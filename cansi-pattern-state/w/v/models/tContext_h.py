"""Classe de template."""
from .factory import Factory


class TContext_h(Factory):
    """Classe de template."""
    def __init__(self, data_model, template_name):

        Factory.__init__(self, template_name)

        self.data_model = data_model

        self.tmpl.name = "Context_h"

        self.tmpl.state = data_model['state']

    def put(self):
        fileName = "%s.h" % self.tmpl.state['context']['name']
        print ("File: %s" % fileName)
        print self.tmpl

    def save(self):
        fileName = "%s.h" % self.tmpl.state['context']['name']
        print ("Save File: %s" % fileName)
        open(fileName, 'w').write(str(self.tmpl))

