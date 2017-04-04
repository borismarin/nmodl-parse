class NModl(object):
    BLOCKS = ['title', 'assigned', 'solve', 'parameter', 'derivative',
              'state', 'procedure', 'function', 'iniial', 'breakpoint']

    def __init__(self, mod_string):
        from nmodl.program import program
        self.parsed = program.parseString(mod_string)

    def interpret(self):
        for b in self.BLOCKS:
            if self.parsed.get(b, None):
                interpreter = getattr(self, 'interpret_' + b, self.nothing)
                interpreter(self.parsed.get(b))

    def nothing(self, _):
        pass

    def interpret_title(self, title_blk):
        self.title = title_blk['title']

    def interpret_state(self, state_blk):
        self.state = state_blk['state_vars']

    def unparse(self):
        pass
