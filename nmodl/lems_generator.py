from xml.etree.ElementTree import Element, SubElement, tostring

#  TODO: real unit handling
mod_to_lems_units = {
    'mV': ('voltage', 'mV'),
    'S/cm2': ('conductanceDensity', 'S_per_cm2'),
    'ms': ('time', 'ms'),
    'mA/cm2': ('currentDensity', 'mA_per_cm2'),
    '': ('none', '')
}


class NModlVisitor(object):
    BLOCKS = ['title', 'assigned', 'neuron', 'solve', 'parameter',
              'derivative', 'state', 'procedure', 'function', 'initial',
              'breakpoint']  # order MATTERS!

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
    context_mangler = [{'v': 'V'}]  # map global v to adimensional V
    id = ''

    def visit_neuron(self, nrn_blk):
        _, suff = nrn_blk.suffix
        self.id = suff + '_lems'
        self.comptype = SubElement(self.root, 'ComponentType',
                                   attrib={'id': self.id,
                                           'name': self.id,
                                           'extends':
                                           'baseIonChannel'})

    def visit_state(self, state_blk):
        pass

    def visit_parameter(self, param_blk):
        par_vals = {}
        for pd in param_blk.parameters:
            dim, unit = mod_to_lems_units[pd.unit]
            SubElement(self.comptype, 'Parameter', attrib={
                'name': pd.id,
                'dimension': dim
            })
            par_vals[pd.id] = pd.value + ' ' + unit
        self.create_component(par_vals)

    def extra_comptype_defs(self):
        # elements that don't come from parsing
        mv = Element('Constant', attrib={
            'dimension': 'voltage',
            'name': 'MV',
            'value': '1mV',
        })
        ms = Element('Constant', attrib={
            'dimension': 'time',
            'name': 'MS',
            'value': '1ms',
        })
        reqv = Element('Requirement', attrib={
            'name': 'v',
            'dimension': 'voltage',
        })
        self.comptype.append(mv)
        self.comptype.append(ms)
        self.comptype.append(reqv)

    def create_component(self, par_vals):
        comp_attr = {'id': self.id}
        comp_attr.update(par_vals)
        self.component = SubElement(self.root, self.id, attrib=comp_attr)

    def render(self):
        self.extra_comptype_defs()
        return tostring(self.root)
