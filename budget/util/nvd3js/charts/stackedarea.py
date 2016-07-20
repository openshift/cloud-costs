from ..nvd3js import Nvd3js

class StackedAreaChart(Nvd3js):
    _chart = "stackedAreaChart"

    def options(self):
        pass

    def __init__(self, **kwargs):
        super(StackedAreaChart, self).__init__(**kwargs)

    def __html__(self):
        ''' used by tal:replace '''
        return self._js_ % dict(
                                    chart = self._chart,
                                    options = self.options(),
                                    data = self.data
                                )
