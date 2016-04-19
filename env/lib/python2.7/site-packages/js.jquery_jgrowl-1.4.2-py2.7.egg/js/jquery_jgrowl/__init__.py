from fanstatic import Library, Resource

from js.jquery import jquery

library = Library('jquery_jgrowl', 'resources')

jquery_jgrowl_css = Resource(library, 'jquery.jgrowl.css')

jquery_jgrowl = Resource(
    library, 'jquery.jgrowl.js',
    minified='jquery.jgrowl.min.js',
    depends=[jquery, jquery_jgrowl_css])
