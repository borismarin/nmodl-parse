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

    def visit(self, parsed):
        for b in self.BLOCKS:
            blk = parsed.get(b, None)
            if blk:
                getattr(self, 'visit_' + b, self.nothing)(blk)

    def nothing(self, _):
        pass


class LemsCompTypeGenerator(NModlVisitor):

    context_mangler = [{'v': 'V'}]  # map global v to adimensional V
    id = ''

    def visit_neuron(self, nrn_blk):
        _, suff = nrn_blk.suffix
        self.id = suff + '_lems'
        self.comp_type = Element('ComponentType',
                                 attrib={'id': self.id,
                                         'name': self.id,
                                         'extends':
                                         'baseIonChannel'})

    def visit_state(self, state_blk):
        pass

    def visit_parameter(self, param_blk):
        for pd in param_blk.parameters:
            dim, unit = mod_to_lems_units[pd.unit]
            SubElement(self.comp_type, 'Parameter', attrib={
                'name': pd.id,
                'dimension': dim
            })

    def extra_comp_type_defs(self):
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
        self.comp_type.append(mv)
        self.comp_type.append(ms)
        self.comp_type.append(reqv)

    def generate(self, parsed):
        self.visit(parsed)
        self.extra_comp_type_defs()
        return self.comp_type


class LemsComponentGenerator(NModlVisitor):

    def visit_neuron(self, nrn_blk):
        _, suff = nrn_blk.suffix
        self.id = suff + '_lems'

    def visit_parameter(self, param_blk):
        self.par_vals = {}
        for pd in param_blk.parameters:
            dim, unit = mod_to_lems_units[pd.unit]
            self.par_vals[pd.id] = pd.value + ' ' + unit

    def generate(self, parsed):
        self.visit(parsed)
        comp_attr = {'id': self.id}
        comp_attr.update(self.par_vals)
        return Element(self.id, attrib=comp_attr)


def Mod2NeuroMLLems(mod_string):

    from nmodl.program import program
    parsed = program.parseString(mod_string)

    root = Element('neuroml')
    root.append(LemsCompTypeGenerator().generate(parsed))
    root.append(LemsComponentGenerator().generate(parsed))

    return tostring(root)
