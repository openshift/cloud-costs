from ..nvd3js import Nvd3js

class HistoricalBarChart(Nvd3js):
    _chart = "historicalBarChart"

    def options(self):
        return '''
            .margin({top: %(top_margin)i, right: %(right_margin)i, bottom: %(bottom_margin)i, left: %(left_margin)i})
            .width(%(width)s)
            .height(%(height)s)
            .duration(%(duration)i)
            .showXAxis(%(show_xaxis)s)
            .showYAxis(%(show_yaxis)s)
        ''' % dict(
                top_margin=self.top_margin,
                right_margin=self.right_margin,
                bottom_margin=self.bottom_margin,
                left_margin=self.left_margin,
                width=self.width,
                height=self.height,
                show_xaxis=self.show_xaxis,
                show_yaxis=self.show_yaxis,
                duration=self.duration,
            )

    def __init__(self, **kwargs):
        self.top_margin = 15
        self.right_margin = 10
        self.bottom_margin = 50
        self.left_margin = 60
        self.width = 'null'
        self.height = 'null'
        self.show_xaxis = 'true'
        self.show_yaxis = 'true'
        self.duration = 250

        super(HistoricalBarChart, self).__init__(**kwargs)

    def __html__(self):
        ''' used by tal:replace '''
        return self._js_ % dict(
                                    chart = self._chart,
                                    options = self.options(),
                                    data = self.data
                                )
