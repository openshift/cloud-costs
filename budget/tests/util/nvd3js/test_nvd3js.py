import unittest
from budget.util.nvd3js import *

#TODO: These are really naive tests.
#
# Eventually they should include an attempt to ensure we're emitting valid
# javascript.
class TestBoxPlotChart(unittest.TestCase):
    def runTest(self):
        chart_name = "boxPlotChart"
        chart = BoxPlotChart()
        self.assertRegexpMatches(chart.__html__(), 'nv\.models\.%s' % chart_name)

class TestBulletChart(unittest.TestCase):
    def runTest(self):
        chart_name = "bulletChart"
        chart = BulletChart()
        self.assertRegexpMatches(chart.__html__(), 'nv\.models\.%s' % chart_name)

class TestCandlestickBarChart(unittest.TestCase):
    def runTest(self):
        chart_name = "candlestickBarChart"
        chart = CandlestickBarChart()
        self.assertRegexpMatches(chart.__html__(), 'nv\.models\.%s' % chart_name)

class TestCumulativeLineChart(unittest.TestCase):
    def runTest(self):
        chart_name = "cumulativeLineChart"
        chart = CumulativeLineChart()
        self.assertRegexpMatches(chart.__html__(), 'nv\.models\.%s' % chart_name)

class TestDiscreteBarChart(unittest.TestCase):
    def runTest(self):
        chart_name = "discreteBarChart"
        chart = DiscreteBarChart()
        self.assertRegexpMatches(chart.__html__(), 'nv\.models\.%s' % chart_name)

class TestHistoricalBarChart(unittest.TestCase):
    def runTest(self):
        chart_name = "historicalBarChart"
        chart = HistoricalBarChart()
        self.assertRegexpMatches(chart.__html__(), 'nv\.models\.%s' % chart_name)

class TestLineChart(unittest.TestCase):
    def runTest(self):
        chart_name = "lineChart"
        chart = LineChart()
        self.assertRegexpMatches(chart.__html__(), 'nv\.models\.%s' % chart_name)

class TestLinePlusBarChart(unittest.TestCase):
    def runTest(self):
        chart_name = "linePlusBarChart"
        chart = LinePlusBarChart()
        self.assertRegexpMatches(chart.__html__(), 'nv\.models\.%s' % chart_name)

class TestLineWithFocusChart(unittest.TestCase):
    def runTest(self):
        chart_name = "lineWithFocusChart"
        chart = LineWithFocusChart()
        self.assertRegexpMatches(chart.__html__(), 'nv\.models\.%s' % chart_name)

class TestMultiBarChart(unittest.TestCase):
    def runTest(self):
        chart_name = "multiBarChart"
        chart = MultiBarChart()
        self.assertRegexpMatches(chart.__html__(), 'nv\.models\.%s' % chart_name)

class TestMultibarHorizontalChart(unittest.TestCase):
    def runTest(self):
        chart_name = "multibarHorizontalChart"
        chart = MultibarHorizontalChart()
        self.assertRegexpMatches(chart.__html__(), 'nv\.models\.%s' % chart_name)

class TestMultiChart(unittest.TestCase):
    def runTest(self):
        chart_name = "multiChart"
        chart = MultiChart()
        self.assertRegexpMatches(chart.__html__(), 'nv\.models\.%s' % chart_name)

class TestOhlcBarChart(unittest.TestCase):
    def runTest(self):
        chart_name = "ohlcBarChart"
        chart = OhlcBarChart()
        self.assertRegexpMatches(chart.__html__(), 'nv\.models\.%s' % chart_name)

class TestParallelCoordinatesChart(unittest.TestCase):
    def runTest(self):
        chart_name = "parallelCoordinatesChart"
        chart = ParallelCoordinatesChart()
        self.assertRegexpMatches(chart.__html__(), 'nv\.models\.%s' % chart_name)

class TestPieChart(unittest.TestCase):
    def runTest(self):
        chart_name = "pieChart"
        chart = PieChart()
        self.assertRegexpMatches(chart.__html__(), 'nv\.models\.%s' % chart_name)

class TestScatterChart(unittest.TestCase):
    def runTest(self):
        chart_name = "scatterChart"
        chart = ScatterChart()
        self.assertRegexpMatches(chart.__html__(), 'nv\.models\.%s' % chart_name)

class TestSparklinePlus(unittest.TestCase):
    def runTest(self):
        chart_name = "sparklinePlus"
        chart = SparklinePlus()
        self.assertRegexpMatches(chart.__html__(), 'nv\.models\.%s' % chart_name)

class TestStackedAreaChart(unittest.TestCase):
    def runTest(self):
        chart_name = "stackedAreaChart"
        chart = StackedAreaChart()
        self.assertRegexpMatches(chart.__html__(), 'nv\.models\.%s' % chart_name)

class TestSunburstChart(unittest.TestCase):
    def runTest(self):
        chart_name = "sunburstChart"
        chart = SunburstChart()
        self.assertRegexpMatches(chart.__html__(), 'nv\.models\.%s' % chart_name)
