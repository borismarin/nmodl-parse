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
              'derivative', 'state', 'procedures', 'functions', 'initial',
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
    units = {'': 'none'}

    def visit_assigned(self, assign_blk):
        for adef in assign_blk.assigneds:
            self.units[adef.id] = adef.unit

    def visit_neuron(self, nrn_blk):
        self.id = nrn_blk.suffix + '_lems'
        self.comp_type = self.xml_element('ComponentType',
                                          {'id': self.id,
                                           'name': self.id,
                                           'extends': 'baseIonChannel'})
        self.exposures_requires(nrn_blk.use_ions)

    def named_dimensional(self, exp_req_par, var, unit=None):
        if unit is None:
            unit = mod_to_lems_units[self.units[var]][0]
        else:
            self.units[var] = unit
        self.xml_element(exp_req_par,
                         {'name': var, 'dimension': unit},
                         parent=self.comp_type)

    def exposures_requires(self, use_ions):
        for ui in use_ions:
            for r in ui.reads:
                self.named_dimensional('Requirement', r)
            for w in ui.writes:
                self.named_dimensional('Exposure', w)

    def visit_state(self, state_blk):
        for sv in state_blk.state_vars:
            unit = sv.unit if sv.unit else 'none'
            self.named_dimensional('Exposure', sv.id, unit)

    def visit_parameter(self, param_blk):
        for pd in param_blk.parameters:
            unit = pd.unit if pd.unit else 'none'
            self.named_dimensional('Parameter', pd.id, unit)

    def visit_functions(self, func_blk):
        for f in func_blk:
            pass

    def extra_comp_type_defs(self):
        # elements that don't come from parsing
        self.xml_element('Constant',
                         {'dimension': 'voltage', 'name': 'MV', 'value': '1mV'},
                         parent=self.comp_type)
        self.xml_element('Constant',
                         {'dimension': 'time', 'name': 'MS', 'value': '1ms'},
                         parent=self.comp_type)
        self.xml_element('Requirement',
                         {'name': 'v', 'dimension': 'voltage'},
                         parent=self.comp_type)

    def xml_element(self, name, attribs, parent=None):
        if parent is None:
            return Element(name, attrib=attribs)
        else:
            return SubElement(parent, name, attrib=attribs)

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
