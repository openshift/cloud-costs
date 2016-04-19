from fanstatic import Library, Resource, Group
from js.jqueryui import jqueryui

library = Library('jqueryui_selectmenu', 'resources')

# Define the resources in the library like this.
# For options and examples, see the fanstatic documentation.
selectmenu_js = Resource(library, 'jquery.ui.selectmenu.js',
                         depends=[jqueryui])
selectmenu_css = Resource(library, 'jquery.ui.selectmenu.css')
selectmenu = Group([selectmenu_js, selectmenu_css])
