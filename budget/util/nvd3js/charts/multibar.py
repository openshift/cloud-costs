from ..nvd3js import Nvd3js

class MultiBarChart(Nvd3js):
    _chart = "multiBarChart"

    def options(self):
        opts = '''
            .staggerLabels(%(stagger_labels)s)
            .margin({top: %(top_margin)i, right: %(right_margin)i, bottom: %(bottom_margin)i, left: %(left_margin)i})
            .width(%(width)s)
            .height(%(height)s)
            .showXAxis(%(show_xaxis)s)
            .showYAxis(%(show_yaxis)s)
            .duration(%(duration)i)
            .showControls(%(show_controls)s)
            .reduceXTicks(%(reduce_xticks)s);

        chart.stacked(true)
        ''' % dict(
                stagger_labels=self.stagger_labels,
                top_margin=self.top_margin,
                right_margin=self.right_margin,
                bottom_margin=self.bottom_margin,
                left_margin=self.left_margin,
                width=self.width,
                height=self.height,
                show_xaxis=self.show_xaxis,
                show_yaxis=self.show_yaxis,
                duration=self.duration,
                show_controls=self.show_controls,
                reduce_xticks=self.reduce_xticks,
            )
        return opts

    def __init__(self, **kwargs):
        self.stagger_labels = 'false'
        self.top_margin = 15
        self.right_margin = 10
        self.bottom_margin = 50
        self.left_margin = 60
        self.width = 'null'
        self.height = 'null'
        self.show_xaxis = 'true'
        self.show_yaxis = 'true'
        self.duration = 250
        self.show_controls = 'true'
        self.reduce_xticks = 'false'

        super(MultiBarChart, self).__init__(**kwargs)

    def __html__(self):
        ''' used by tal:replace '''
        return self._js_ % dict(
                                    chart = self._chart,
                                    options = self.options(),
                                    data = self.data
                                )
