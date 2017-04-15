class NModl(object):
    BLOCKS = ['title', 'assigned', 'parameter', 'neuron', 'units', 'state',
              'derivative', 'procedure', 'function', 'initial', 'breakpoint']

    '''
    --PARAMETERs are GLOBAL by default, and visible from hoc
    --STATEs are RANGE by default, and visible from hoc
    --mechanism-specific ASSIGNED variables are RANGE by default, but they are
    not visible from hoc unless they also appear in a GLOBAL or RANGE statement
    in the NEURON block
    --ASSIGNED variables that are not mechanism-specific (v, celsius, t, dt,
    diam, area) _are_ visible from hoc but are not mentioned in the NEURON
    block. celsius is not a RANGE variable.
    '''

    def __init__(self, mod_string):
        from nmodl.program import program
        self.parsed = program.parseString(mod_string)
        self.parameters = {}
        self.state = {}
        self.requires = {}
        self.exposes = {}
        self.id = ''
        self.units = {'': 'none'}

    def visit(self):
        for b in self.BLOCKS:
            blk = self.parsed.get(b, None)
            if blk:
                getattr(self, 'visit_' + b, self.generic_visit)(blk)
        self.post_visit()

    def generic_visit(self, _):
        pass

    def visit_title(self, title_blk):
        self.title = title_blk.title

    def visit_assigned(self, assign_blk):
        for adef in assign_blk.assigneds:
            self.units[adef.id] = adef.unit

    def visit_neuron(self, nrn_blk):
        s_, suff = nrn_blk.suffix
        self.id = suff
        for ui in nrn_blk.use_ions:
            for r in ui.read:
                self.requires[r] = self.units[r]
            for w in ui.write:
                self.exposes[w] = self.units[w]

    def visit_state(self, state_blk):
        for s in state_blk.state_vars:
            self.state[s] = None

    def visit_parameter(self, param_blk):
        for pdef in param_blk.parameters:
            self.units[pdef.id] = pdef.unit
            self.parameters[pdef.id] = (float(pdef.value), pdef.unit)

    def post_visit(self):
        self.add_default_requires()

    def add_default_requires(self):
        for v in ['v', 'celsius', 'area', 'diam']:
            if v in self.units:
                self.requires[v] = self.units[v]

