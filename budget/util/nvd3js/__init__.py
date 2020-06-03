# nvd3js module

import logging

class Nvd3js (object):
    ''' wrapper for emitting nvd3 javascript glue
        See http://nvd3.org for more info.

        Nearly all class paramaters are pass-throughs to the
        javascript. Please refer to the nvd3 documentation on those.
        See: https://nvd3-community.github.io/nvd3/examples/documentation.html
    '''

    # JavaScript template to be rendered
    _js_ = '''
<script type="text/javascript">
nv.addGraph(function() {
  var chart = nv.models.%(chart)s()%(options)s;

  chart.legend.vers('%(legend)s');

  %(extra)s

  d3.select("#chart svg")
        .datum(data())
        .transition()
        .call(chart);

  nv.utils.windowResize(chart.update);

  return chart;
});

function data() {
  return %(data)s;
}
</script>
    '''

    # This should match the name of the javascript chart class being called
    _chart_ = 'Subclasses override this.'

    _log_ = logging.getLogger(__name__)

    def __init__(self, **kwargs):
        ''' subclasses should override __init__() if they need to override _out_ to
            include additional default values callers shouldn't need to worry
            about.

            There are two features of this class that implementors will care
            about.

            1. Class attributes are used to set all public class variables.
            2. For any additional javascript that needs to be emitted, there is
                the "extra" parameter, which can be set to any string of javascript
                as needed.
        '''
        self.data = []
        self._out_ = []

        for key, value in kwargs.items():
            setattr(self, key, value)

        if not getattr(self, 'legend', None):
            self.legend = 'furious' # default to new "furious" legend

        if not getattr(self, 'extra', None):
            self.extra = ""

    def __html__(self):
        ''' used by tal:replace '''
        js = self._js_ % dict(chart=self._chart_,
                            options=self.options(),
                            data=self.data,
                            extra=self.extra,
                            legend=self.legend)

        self._log_.debug('Rendering chart: %s' % js)
        return js

    def options(self):
        ''' provides the chained calls to set optional attributes on the chart
            class
        '''
        denylist = [ 'data', '_out_', 'extra', 'legend' ]
        out = self._out_

        for k, v in self.__dict__.items():
            if k in denylist:
                continue
            out.append('.%s(%s)' % (k,self._value_map(v)))
        return ''.join(out)

    def _setdefault(self, name, default=None, **kwargs):
        if name in kwargs:
            setattr(self, name, kwargs[name])
        else:
            setattr(self, name, default)

    def _value_map(self, value):
        if isinstance(value, bool):
            return str(value).lower()
        elif isinstance(value, list):
            return str(value)
        elif isinstance(value, dict):
            return str(value)
        elif value == 'null':
            return str(value)
        else:
            return "'%s'" % str(value)



class BoxPlotChart(Nvd3js):
    _chart_ = "boxPlotChart"

class BulletChart(Nvd3js):
    _chart_ = "bulletChart"

class CandlestickBarChart(Nvd3js):
    _chart_ = "candlestickBarChart"

class CumulativeLineChart(Nvd3js):
    _chart_ = "cumulativeLineChart"

class DiscreteBarChart(Nvd3js):
    _chart_ = "discreteBarChart"
    # Graph Data:
    #
    # [
    #     { 'key' : 'foo',
    #       'values' : [
    #             {'label' : 'foo', 'value' : 10 },
    #             {'label' : 'bar', 'value' : 20 }
    #         ]
    #     },
    # ]
    def __init__(self, **kwargs):
        super(DiscreteBarChart, self).__init__(**kwargs)
        self._out_ = [ '.x(function(d) { return d.label })',
                        '.y(function(d) { return d.value })' ]

class HistoricalBarChart(Nvd3js):
    _chart_ = "historicalBarChart"

class LineChart(Nvd3js):
    _chart_ = "lineChart"

class LinePlusBarChart(Nvd3js):
    _chart_ = "linePlusBarChart"

class LineWithFocusChart(Nvd3js):
    _chart_ = "lineWithFocusChart"

class MultiBarChart(Nvd3js):
    _chart_ = "multiBarChart"

class MultibarHorizontalChart(Nvd3js):
    _chart_ = "multibarHorizontalChart"

class MultiChart(Nvd3js):
    _chart_ = "multiChart"

class OhlcBarChart(Nvd3js):
    _chart_ = "ohlcBarChart"

class ParallelCoordinatesChart(Nvd3js):
    _chart_ = "parallelCoordinatesChart"

class PieChart(Nvd3js):
    _chart_ = "pieChart"
    # Graph Data:
    #
    # [
    # {'label': 'foo', 'value': 10 },
    # {'label': 'bar', 'value': 20 }
    # ]
    def __init__(self, **kwargs):
        super(PieChart, self).__init__(**kwargs)
        self._out_ = [ '.x(function(d) { return d.label })',
                        '.y(function(d) { return d.value })' ]

class ScatterChart(Nvd3js):
    _chart_ = "scatterChart"

class SparklinePlus(Nvd3js):
    _chart_ = "sparklinePlus"

class StackedAreaChart(Nvd3js):
    _chart_ = "stackedAreaChart"
    # Graph Data:
    #
    # Each dict of values must be the same length.
    #
    # Coord values must be numeric. Use nAxis.tickFormat() to transform
    # coordinate values, as needed.
    #
    # [
    #    { 'key': label1, 'values': [[x1,y1],[x2,y2]] },
    #    { 'key': label2, 'values': [[x1,y1],[x2,y2]] },
    # ]
    def __init__(self, **kwargs):
        super(StackedAreaChart, self).__init__(**kwargs)
        self._out_ = [ '.x(function(d) { return d[0] })',
                        '.y(function(d) { return d[1] })' ]

class SunburstChart(Nvd3js):
    _chart_ = "sunburstChart"
