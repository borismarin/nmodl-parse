class NModl(object):
    BLOCKS = ['title', 'assigned', 'solve', 'parameter', 'derivative',
              'state', 'procedure', 'function', 'iniial', 'breakpoint']

    def __init__(self, mod_string):
        from nmodl.program import program
        self.parsed = program.parseString(mod_string)
        self.parameters = {}
        self.state = {}

    def visit(self):
        for b in self.BLOCKS:
            blk = self.parsed.get(b, None)
            if blk:
                getattr(self, 'visit_' + b, self.nothing)(blk)

    def nothing(self, _):
        pass

    def visit_title(self, title_blk):
        self.title = title_blk['title']

    def visit_state(self, state_blk):
        for s in state_blk.state_vars:
            self.state[s] = None

    def visit_parameter(self, param_blk):
        for pdef in param_blk.parameters:
            try:
                self.parameters[pdef.name] = float(pdef.val)
            except ValueError:  # no or crazy val specified
                self.parameters[pdef.name] = None
