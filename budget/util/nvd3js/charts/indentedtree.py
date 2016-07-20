from ..nvd3js import Nvd3js

class IndentedTree(Nvd3js):
    _chart = "indentedTree"

    def options(self):
        return ''' '''

    def __init__(self, **kwargs):
        super(IndentedTree, self).__init__(**kwargs)

    def __html__(self):
        ''' used by tal:replace '''
        return self._js_ % dict(
                                    chart = self._chart,
                                    options = self.options(),
                                    data = self.data
                                )

