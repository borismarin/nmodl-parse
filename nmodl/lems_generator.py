from xml.etree.ElementTree import Element, SubElement, tostring


class NModlVisitor(object):
    BLOCKS = ['title', 'assigned', 'solve', 'parameter', 'derivative', 'state',
              'procedure', 'function', 'initial', 'breakpoint', 'neuron']

    def __init__(self, mod_string):
        from nmodl.program import program
        self.parsed = program.parseString(mod_string)

    def visit(self):
        for b in self.BLOCKS:
            blk = self.parsed.get(b, None)
            if blk:
                getattr(self, 'visit_' + b, self.nothing)(blk)

    def nothing(self, _):
        pass


class NeuroMLLemsGenerator(NModlVisitor):

    root = Element('neuroml')

    def visit_neuron(self, nrn_blk):
        name = nrn_blk.suffix[1] + '_lems'
        SubElement(self.root, 'ComponentType',
                   attrib={'id': name,
                           'name': name,
                           'extends': 'baseIonChannel'})

    def visit_state(self, state_blk):
        pass

    def visit_parameter(self, param_blk):
        pass

    def render(self):
        return tostring(self.root)
