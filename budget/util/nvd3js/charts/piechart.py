from ..nvd3js import Nvd3js

class PieChart(Nvd3js):
    _chart = "pieChart"

    def options(self):
        return '''
            .x(function(d) { return d.label })
            .y(function(d) { return d.value })
            .showLabels(%(show_labels)s)
            .margin({top: %(top_margin)i, right: %(right_margin)i, bottom: %(bottom_margin)i, left: %(left_margin)i})
            .width(%(width)s)
            .height(%(height)s)
            .showLegend(%(show_legend)s)
            .legendPosition('%(legend_position)s')
            .duration(%(duration)i)
        ''' % dict(
                show_labels=self.show_labels,
                top_margin=self.top_margin,
                right_margin=self.right_margin,
                bottom_margin=self.bottom_margin,
                left_margin=self.left_margin,
                width=self.width,
                height=self.height,
                show_legend=self.show_legend,
                legend_position=self.legend_position,
                duration=self.duration
        )

    def __init__(self, **kwargs):
        self.show_labels = 'true'
        self.top_margin = 30
        self.right_margin = 20
        self.bottom_margin = 20
        self.left_margin = 20
        self.width = 'null'
        self.height = 'null'
        self.show_legend = 'true'
        self.legend_position = 'top'
        self.duration = 250

        super(PieChart, self)

    def __html__(self):
        ''' used by tal:replace '''
        return self._js_ % dict(
                                    chart = self._chart,
                                    options = self.options(),
                                    data = self.data
                                )
