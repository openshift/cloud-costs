from fanstatic import Library, Resource

library = Library('tinymce', 'resources')

tinymce = Resource(library, 'tinymce.js', minified='tinymce.min.js')
