import locale
import logging

from decimal import Decimal, getcontext
# The TreeTable JS module we're using needs us to identify parent-child
# relationships in our hierarchy. Each label needs to be unique, but isn't
# otherwise meaningful. Randomly generated UUIDs seems like the right fit
# for that.
from uuid import uuid4 as uuid

locale.setlocale(locale.LC_ALL, "en_US")
log = logging.getLogger(__name__)

class Branch(object):
    ''' helper object used for calculating line item costs within a category '''
    def __init__(self, **kwargs):
        self.parent = None
        self.children = []
        self.uuid = uuid()
        self.name = self.__class__
        self.datatype = 'Branch'

        for arg,val in kwargs.iteritems():
            setattr(self, arg, val)

    def __repr__(self):
        return str(self.uuid)

    def get_child_by_name(self, name):
        # Each parent's children is expected to have a unique name among
        # its siblings.
        #
        # Different parents can have children with the same name, however.
        for child in self.children:
            if child.name == name:
                return child
        return None

    def total_cost(self):
        # don't double-count the totals.
        if self.name == 'Total':
            return None

        total = 0
        for child in self.children:
            c = child.total_cost()
            if c:
                total += c
        return total

    def dump(self, include_leaves=True):
        ''' traverse our children and return a sanitized list of our
            __dict__ and our children's __dict__
        '''

        blacklist = ['children']
        out = []
        me = {}

        # Don't show any entries that don't have line items on this
        # invoice.
        if self.has_leaf() and self.total_cost():
            me['total_cost'] = locale.currency(self.total_cost(), grouping=True)
        else:
            return []

        for k,v in self.__dict__.iteritems():
            if k not in blacklist:
                me[k] = str(v)
        out.append(me)
        for child in self.children:
            if include_leaves:
                if getattr(child, 'children', None) or isinstance(child, Leaf):
                    out.extend(child.dump())
            else:
                if isinstance(child, Branch):
                    out.extend(child.dump(include_leaves))
        return out

    def has_leaf(self):
        ''' traverse our children, return Boolean about whether we have any
            Leaf objects in the tree
        '''
        for child in self.children:
            if isinstance(child, Leaf):
                return True
            elif isinstance(child, Branch):
                if child.has_leaf():
                    return True
        return False

class Leaf(object):
    ''' helper object used for calculating line item costs within a category '''
    def __init__(self, **kwargs):
        self.parent = None
        self.uuid = uuid()
        self.name = self.__class__
        self.content = None
        self.datatype = 'Leaf'

        for arg,val in kwargs.iteritems():
            setattr(self, arg, val)

    def total_cost(self):
        return self.content['total_cost']

    def dump(self):
        rendered_content = {}
        for k,v in self.content.iteritems():
            if isinstance(v, Decimal):
                rendered_content[k] = locale.currency(v, grouping=True)
            elif isinstance(v, float):
                rendered_content[k] = locale.format('%.4f', v, grouping=True)
            else:
                rendered_content[k] = str(v)

        return [{'uuid':self.uuid,
                'parent':self.parent,
                'content':rendered_content}]

