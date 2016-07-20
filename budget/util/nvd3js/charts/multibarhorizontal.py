from ..nvd3js import Nvd3js

class MultibarHorizontalChart(Nvd3js):
    _chart = "multibarHorizontalChart"

    def options(self):
        return ''' '''

    def __init__(self, **kwargs):
        super(MultibarHorizontalChart, self).__init__(**kwargs)

    def __html__(self):
        ''' used by tal:replace '''
        return self._js_ % dict(
                                    chart = self._chart,
                                    options = self.options(),
                                    data = self.data
                                )

