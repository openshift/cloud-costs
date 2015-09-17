# wrapper for emitting nvd3 javascrpt glue

class Nvd3js (object):
    _js_ = '''
<script type="text/javascript">
nv.addGraph(function() {
  var chart = nv.models.%(chart)s()%(options)s;

    d3.select("#chart svg")
        .datum(data())
        .transition().duration(350)
        .call(chart);

  return chart;
});

function data() {
  return %(data)s;
}
</script>
    '''

    def __init__(self, **kwargs):
        self.data = []

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __html__(self):
        ''' used by tal:replace '''
        return "<h1>UNIMPLEMENTED</h1>"

