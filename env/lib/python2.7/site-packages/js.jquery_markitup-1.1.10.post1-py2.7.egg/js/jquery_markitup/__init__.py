from fanstatic import Library, Resource, Group
from js.jquery import jquery

library = Library('markitup', 'resources')

# Define the resources in the library like this.
# For options and examples, see the fanstatic documentation.
# resource1 = Resource(library, 'style.css')


simple_style = Resource(library, "markitup/skins/simple/style.css")
markitup_style = Resource(library, "markitup/skins/markitup/style.css")

default_set_css = Resource(library, "markitup/sets/default/style.css")
default_set = Resource(library, "markitup/sets/default/set.js",
                       depends=[default_set_css])

markitup = Resource(library, "markitup/jquery.markitup.js",
                    depends=[jquery])
