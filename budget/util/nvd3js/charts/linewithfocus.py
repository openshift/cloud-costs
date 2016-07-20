from ..nvd3js import Nvd3js

class LineWithFocusChart(Nvd3js):
    _chart = "lineWithFocusChart"

    def options(self):
        return ''' '''

    def __init__(self, **kwargs):
        super(LineWithFocusChart, self).__init__(**kwargs)

    def __html__(self):
        ''' used by tal:replace '''
        return self._js_ % dict(
                                    chart = self._chart,
                                    options = self.options(),
                                    data = self.data
                                )

