import urllib
from warnings import warn
from lxml import etree
import zipfile
import StringIO
try:
    import json
except ImportError:
    import simplejson as json
from pkg_resources import get_distribution
import shutil
import os
import tempfile
import re

jqueryui_download_url = 'http://jqueryui.com/download'
online_yui_compressor_url = 'http://www.refresh-sf.com/yui/'

# We're not using fanstatic.codegen because:
#
# 1. It can not deal with external dependencies (in our case js.jquery.jquery)
#
# 2. It can not deal with libraries whose registered name is different
#    than its python name. I.e. we want:
#
#       library = Library('jqueryui', 'resources')
#
#    but generate_code() gives:
#
#       jqueryui = Library('jqueryui', 'resources')

def decustomize(filename):
    custom_cruft = re.compile(r'''
        -\d+(\.\d+)*                    # version number
        \.custom                        # ".custom"
        (?=                             # followed by...
            (\.min)?                    # optional ".min"
            (\.css|\.js)?               # optional ".css" or ".js"
            \Z                          # end of string
        )
    ''', re.X)
    return custom_cruft.sub('', filename)


class Download(object):
    def __init__(self, archive):
        self.archive = archive

    def unpack(self, dest_dir, path_mapper):
        archive = self.archive
        for path in archive.namelist():
            extract_path = path_mapper(path)
            if extract_path is None:
                continue
            dest = os.path.join(dest_dir, extract_path)
            if not os.path.isdir(os.path.dirname(dest)):
                os.makedirs(os.path.dirname(dest))
            file(dest, "wb").write(archive.read(path))

    def unpack_js(self, dest_dir):
        def path_mapper(path):
            if path.startswith('development-bundle/ui/'):
                path = path[len('development-bundle/ui/'):]
            elif path.startswith('js/jquery-ui') and path.endswith('.min.js'):
                # The minified js bundle is not in development-bundle/...
                path = os.path.join('minified', path[len('js/'):])
            else:
                return None
            path = decustomize(path)
            return os.path.join('ui', path)

        return self.unpack(dest_dir, path_mapper)

    def unpack_css(self, dest_dir, include_base=False):
        def path_mapper(path):
            if not path.startswith('development-bundle/themes/'):
                return None
            path = path[len('development-bundle/themes/'):]
            if not include_base and path.startswith('base/'):
                return None
            path = decustomize(path)
            return os.path.join('themes', path)

        return self.unpack(dest_dir, path_mapper)


class DownloadBuilder(object):
    def __init__(self):
        self.download_page_html = etree.parse(jqueryui_download_url,
                                              etree.HTMLParser())

    @property
    def jqueryui_dependencies(self):
        html = self.download_page_html
        dep_js = html.find('//div[@id="content-wrapper"]//script').text
        dep_json = dep_js[dep_js.find('{'):dep_js.find('}') + 1]
        dep_json = dep_json.replace("'", '"')
        return json.loads(dep_json)

    @property
    def stable_version(self):
        html = self.download_page_html
        radio = html.find('//input[@name="ui-version"][@checked]')
        return radio.attrib['value']

    @property
    def theme_info(self):
        html = self.download_page_html
        for option in html.findall('//select[@id="theme"]/option'):
            theme_name = option.text.lower().replace(' ', '-') or 'no-theme'
            theme_params = option.attrib['value']
            yield theme_name, theme_params

    def build(self, theme_name='No Theme', theme_params='none'):
        print 'downloading', theme_name
        inputs = self.download_page_html.findall(
            '//div[@id="download-builder-components"]//input')
        query = {
            'download': 'true',
            'theme': theme_params,
            't-name': theme_name,
            'ui-version': self.stable_version,
            'files[]': [input.attrib['value'] for input in inputs],
            }
        postdata = urllib.urlencode(query, doseq=True)
        theme_zip = urllib.urlopen(jqueryui_download_url, postdata).read()
        archive = zipfile.ZipFile(StringIO.StringIO(theme_zip))
        return Download(archive)


download_builder = []

def get_download_builder():
    if not download_builder:
        ui_version = re.sub(r'(-|dev).*', '',
                            get_distribution('js.jqueryui').version)

        builder = DownloadBuilder()
        download_builder.append(builder)

        # Check current version
        if builder.stable_version != ui_version:
            warn("The current stable version of jQueryUI is %r, not %r"
                 % (builder.stable_version, ui_version))

    return download_builder[0]

def expand_css_imports(filename):
    dir_, base = os.path.split(filename)
    for line in file(filename):
        if line.startswith('@import '):
            import_file = line[line.index('"')+1:line.rindex('"')]
            for line in expand_css_imports(os.path.join(dir_, import_file)):
                yield line
        else:
            yield line

def download(dest_dir):
    builder = get_download_builder()

    temp_dir = tempfile.mkdtemp(dir=os.path.dirname(dest_dir))

    # Build, download, and unpack all themes
    first_build = True
    for theme_name, theme_params in builder.theme_info:
        if theme_params != 'none':
            download = builder.build(theme_name, theme_params)
            if first_build:
                download.unpack_js(temp_dir)
            download.unpack_css(temp_dir, include_base=first_build)
            first_build = False

    # HACK: Build the bundled .css for the base theme.
    # This does not seem to be included in any of the downloads available
    # from the jqueryui downloadbuilder.
    base_bundle = os.path.join(temp_dir, 'themes/base/jquery-ui.css')
    if not os.path.exists(base_bundle):
        all_css = os.path.join(temp_dir, 'themes/base/jquery.ui.all.css')
        file(base_bundle, 'w').writelines(expand_css_imports(all_css))

    # Install the downloaded resources
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.rename(temp_dir, dest_dir)

################################################################

def yui_compress(infile, outfile):
    """ Compress a source file using the online yui compressor
    at http://www.refresh-sf.com/yui/.

    :param string infile: The input file name.
    :param string outfile: The output file name.
    """
    srctypes = {'.css': 'CSS', '.js': 'JS'}

    _, ext = os.path.splitext(infile)
    if ext not in srctypes:
        raise ValueError("unknown file extension for file %r" % infile)

    with file(infile, 'r') as fp:
        input_text = fp.read()

    # Preserve leading comment in compressed ouput
    m = re.match(r'\A(\s*/\*)(?=\s)', input_text)
    if m:
        input_text = m.group(1) + '!' + input_text[m.end():]

    postdata = urllib.urlencode({
        'compresstext': input_text,
        'type': srctypes[ext],
        'redirect': 'on',
        })

    print 'compressing %r to %r' % (infile, outfile)
    result = urllib.urlopen(online_yui_compressor_url, postdata)

    output_dir = os.path.dirname(outfile)
    if output_dir and not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    with file(outfile, 'w') as outfp:
        shutil.copyfileobj(result, outfp)

################################################################

class ResourceInfo(object):
    """ Information about a resource.

    Has the following attributes:

    relpath
        Path to component

    component
        A string identifying the particular component.  For js components
        this should be the same as the component name used in the
        jQueryUI.dependencies object on the jqueryui downloadbuilder
        web page.  E.g 'ui.autocomplete.css'.
        The minified version of a component has the ``component`` name
        as its non-minified version.

    name
        The (python) name used for the component in the js.jqueryui module.

    section
        Section for the resource.  This is used only for grouping the
        resources in the generated python code.

    skip
        If true, we should not emit a resource definition for this resource.

    is_minified
        True iff this is the minified version of a resource

    want_minified
        True iff we really like to have a minified version of this resource

    dependencies
        List of components this resource depends on.

    rollup
        Component which provides a rollup of this one.
    """
    def __init__(self, relpath,
                 component=None,
                 name=None,
                 section=None,
                 skip=False,
                 is_minified=False,
                 want_minified=False,
                 dependencies=None,
                 rollup=None):
        self.relpath = relpath
        self.component = component
        self.name = name
        self.section = section
        self.skip = skip
        self.is_minified = is_minified
        self.want_minified = want_minified
        self.dependencies = dependencies or []
        self.rollup = rollup
        if not self.skip:
            assert self.component and self.name and self.section is not None


class ResourceClassifier(object):
    def __init__(self, *args):
        self.classes = []
        for arg in args:
            self.add_class(**arg)

    def add_class(self, regexp, **info):
        regexp = re.compile(regexp, re.X)
        self.classes.append((regexp, info))

    def __call__(self, relpath):
        dir_, base = os.path.split(relpath)
        split_dir = dir_.split('/')
        base, ext = os.path.splitext(base)

        is_minified = False
        if base.endswith('.min'):
            base = base[:-len('.min')]
            is_minified = True
        if 'minified' in split_dir:
            split_dir.remove('minified')
            dir_ = os.path.join(*split_dir)
            is_minified = True
        deminified = os.path.join(dir_, base + ext)

        for regexp, info in self.classes:
            m = regexp.match(deminified)
            if m:
                info = info.copy()
                for key, value in info.items():
                    if callable(value):
                        info[key] = value(m)
                return ResourceInfo(relpath=relpath,
                                    is_minified=is_minified,
                                    **info)
        return None

def classifier_factory(jqueryui_dependencies):

    SECTION_UI = 0
    SECTION_EFFECTS = 1
    SECTION_THEME = 2
    SECTION_I18N = 3

    def ui_dependencies(component):
        dependencies = jqueryui_dependencies.get(component, [])
        dependencies = [dep for dep in dependencies if dep != 'theme']
        if not dependencies:
            dependencies = ['js.jquery.jquery']
        return dependencies

    def python_safe(name):
        return name.replace('.', '_').replace('-', '_')

    classifier = ResourceClassifier()
    add_class = classifier.add_class
    # .pngs do not get declared as components
    add_class(r'.*\.png',
              skip = True,
              component = None,
              name = None,
              section = None)

    # The js bundle
    add_class(r'ui/jquery-ui\.js',
              component= 'jquery-ui.js',
              name = 'jqueryui',
              dependencies = ['js.jquery.jquery'],
              section = SECTION_UI,
              )
    # The js ui.* components
    add_class(r'ui/jquery\.(?P<comp>ui\.[^/]+)\.js',
              component= lambda m: m.group('comp') + '.js',
              name = lambda m: python_safe(m.group('comp')),
              dependencies = lambda m: ui_dependencies(m.group('comp') + '.js'),
              rollup = 'jquery-ui.js',
              section = SECTION_UI,
              )
    # The js effects.* components
    add_class(r'ui/jquery\.(?P<comp>effects\.[^/]+)\.js',
              component= lambda m: m.group('comp') + '.js',
              name = lambda m: python_safe(m.group('comp')),
              dependencies = lambda m: ui_dependencies(m.group('comp') + '.js'),
              rollup = 'jquery-ui.js',
              section = SECTION_EFFECTS,
              )

    # The i18n bundle
    add_class(r'ui/i18n/jquery-ui-i18n\.js',
              component= 'jquery-ui-i18n.js',
              name = 'jqueryui_i18n',
              dependencies = ['ui.datepicker.js'], # XXX: was 'jquery-ui.js'
              rollup = None,
              section = SECTION_I18N,
              )
    # The i18n components
    add_class(r'ui/i18n/jquery\.ui\.datepicker-(?P<lang>[^/]+)\.js',
              component = lambda m: 'ui.datepicker-' + m.group('lang') + '.js',
              name = lambda m: 'ui_datepicker_' + python_safe(m.group('lang')),
              dependencies = [ 'ui.datepicker.js' ],
              rollup = 'jquery-ui-i18n.js',
              section = SECTION_I18N,
              )

    # The theme bundles
    add_class(r'themes/([^/]+)/jquery-ui\.css',
              component = lambda m: os.path.join(m.group(1), 'jquery-ui.css'),
              name = lambda m: python_safe(m.group(1)),
              want_minified = True,
              dependencies = [],
              rollup = None,
              section = SECTION_THEME,
              )
    # The theme components
    #
    # XXX: Problems:
    #
    #  - These components all "depend" on theme.css (and
    #    core.css), but theme.css needs to be included _after_ the
    #    component.  Right now, this could be done (I think) by
    #    using fanstatic Groups, but it is kind of messy, and
    #    maybe not worth it.
    #
    #  - There are lots of these, leading to a cluttered namespace.
    #    Perhaps they should be in submodules?
    #
    # For now, punt.  Do not declare any fanstatic resources for these.
    #
    add_class(r'themes/([^/]+)/jquery\.ui\.(all|base|core|theme)\.css',
              skip = True,
              )
    add_class(r'themes/([^/]+)/jquery\.([^/]+)\.css',
              skip = True,
              )

    return classifier

def listdir_recursively(top):
    for dirpath, dirnames, filenames in os.walk(top):
        dir_ = dirpath[len(top)+1:]
        for filename in filenames:
            yield os.path.join(dir_, filename)

def compile_resource_declarations(resources_dir):
    dependencies = get_download_builder().jqueryui_dependencies

    classify = classifier_factory(dependencies)

    info_map = {}
    minified = {}
    supersedes = {}

    for relpath in listdir_recursively(resources_dir):
        info = classify(relpath)
        if info is None:
            warn("can not classify %r" % relpath)
        elif info.skip:
            pass
        elif info.is_minified:
            minified[info.component] = info.relpath
        else:
            info_map[info.component] = info
            if info.rollup:
                supersedes.setdefault(info.rollup, []).append(info.name)

    # Compress resources for which we don't have minified versions
    for info in info_map.values():
        if info.want_minified and info.component not in minified:
            # Don't put minified css in 'minified' subdir, so that we
            # don't have to copy the 'images' subdirectory.
            base, ext = os.path.splitext(info.relpath)
            minpath = base + '.min' + ext
            infile = os.path.join(resources_dir, info.relpath)
            outfile = os.path.join(resources_dir, minpath)
            yui_compress(infile, outfile)
            minified[info.component] = minpath

    # Sorting
    #
    # For the sake of readability, we'd like to group the resources
    # in general groups (ui components, effects components, themes, etc...)
    # and even sort them roughly alphabetically within each group.
    # At the same time resources must be declared before any other
    # resources which reference them (either via depends or supersedes).
    #
    # So sort by group and alphabetically, and the adjust the order
    # to make sure that no resources are referenced before they are
    # defined.
    #
    # Note that this can not be done is a single sort operation, because
    # "references" is not a proper partial ordering of the resources.
    # Define "references" to mean "greater than".  (The "less than or equal"
    # is "is not referenced by".)
    # Suppose A references C; also B neither references nor is referenced
    # by either of A or C.  Then we have A <= B and B <= C but A > C.
    # This violates the transitivity requirement for a partial ordering.
    #
    def resolve(dep):
        try:
            return info_map[dep].name
        except KeyError:
            assert dep == 'js.jquery.jquery', dep
            return dep

    remains = sorted(info_map.values(),
                     key=lambda info: (info.section, info.name))
    prev_section = None
    declarations = [
        "from fanstatic import Library, Resource\n",
        "import js.jquery\n",
        "\n",
        "# This code is auto-generated and not PEP8 compliant\n",
        "\n",
        "library = Library('jqueryui', 'resources')\n",
        ]

    while remains:
        for info in remains:
            component = info.component
            depends = [resolve(dep) for dep in info.dependencies]
            references = depends + supersedes.get(component, [])
            if not any(following.name in references for following in remains):
                remains.remove(info)
                break
        else:
            raise AssertionError("circular dependency?")


        args = ['library', repr(info.relpath)]
        if info.dependencies:
            depends = sorted(resolve(dep) for dep in info.dependencies)
            args.append('depends=[%s]' % ', '.join(depends))
        if component in minified:
            args.append('minified=%r' % minified[component])
        if component in supersedes:
            args.append('supersedes=[%s]'
                        % ', '.join(sorted(supersedes[component]))
                        )

        if info.section != prev_section:
            declarations.append("\n")   # blank line between sections
        prev_section = info.section

        declarations.append("%s = Resource(%s)\n"
                            % (info.name, ', '.join(args)))

    return declarations




def main():
    package_dir = os.path.dirname(__file__)
    resources_dir = os.path.join(package_dir, 'resources')
    init_py = os.path.join(package_dir, '__init__.py')

    download(resources_dir)

    code = compile_resource_declarations(resources_dir)
    print "writing", init_py
    file(init_py, 'w').writelines(code)

if __name__ == '__main__':
    main()
