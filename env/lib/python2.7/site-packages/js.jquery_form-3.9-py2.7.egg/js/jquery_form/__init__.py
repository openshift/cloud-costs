import fanstatic
import js.jquery

library = fanstatic.Library('jquery_form', 'resources')

jquery_form = fanstatic.Resource(
    library,
    'jquery.form.js',
    minified='jquery.form.min.js',
    depends=[js.jquery.jquery]
)
