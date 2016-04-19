from fanstatic import Library, Resource

library = Library('jquery', 'resources')

jquery = Resource(library, 'jquery.js', minified='jquery.min.js')
