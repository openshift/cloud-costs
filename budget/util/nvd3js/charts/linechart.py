from ..nvd3js import Nvd3js

class LineChart(Nvd3js):
    _chart = "lineChart"

    def options(self):
        return ''' '''

    def __init__(self, **kwargs):
        super(LineChart, self).__init__(**kwargs)

    def __html__(self):
        ''' used by tal:replace '''
        return self._js_ % dict(
                                    chart = self._chart,
                                    options = self.options(),
                                    data = self.data
                                )
