from ..nvd3js import Nvd3js

class LinePlusBarChart(Nvd3js):
    _chart = "linePlusBarChart"

    def options(self):
        return ''' '''

    def __init__(self, **kwargs):
        super(LinePlusBarChart, self).__init__(**kwargs)

    def __html__(self):
        ''' used by tal:replace '''
        return self._js_ % dict(
                                    chart = self._chart,
                                    options = self.options(),
                                    data = self.data
                                )

