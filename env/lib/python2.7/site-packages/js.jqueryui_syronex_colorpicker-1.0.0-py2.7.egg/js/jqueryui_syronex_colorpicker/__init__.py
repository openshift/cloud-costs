from fanstatic import Library, Resource, Group
from js.jqueryui import jqueryui

library = Library('syronex_colorpicker', 'resources')

# Define the resources in the library like this.
# For options and examples, see the fanstatic documentation.
colorpicker_js = Resource(library, 'syronex-colorpicker.js',
                          depends=[jqueryui])
colorpicker_css = Resource(library, 'syronex-colorpicker.css')
colorpicker = Group([colorpicker_js, colorpicker_css])
