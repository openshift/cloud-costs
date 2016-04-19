from pyramid.scaffolds import PyramidTemplate


class PyramidFanstaticTemplate(PyramidTemplate):
    _template_dir = 'scaffold'
    summary = 'Helpers for Fanstatic integration in Pyramid'

    def post(self, command, output_dir, vars):
        val = PyramidTemplate.post(self, command, output_dir, vars)
        self.out('')
        self.out('Now check README_FANSTATIC.txt to finalize installation')
        return val
