import pyparsing as pp

from nmodl import (assigned, breakpoint, title, parameter, units, procedure,
                   function, state, comment, terminals, initial, neuron,
                   derivative, node)


class Program(node.Node):
    def unpack_parsed(self, parsed):
        for n in ['title', 'units', 'parameter',
                  'neuron', 'derivative',
                  'assigned', 'procedures',
                  'functions', 'breakpoint',
                  'state', 'initial']:
            setattr(self, n, getattr(parsed, n))


program = ((pp.Optional(title.title)('title') &
            pp.Optional(units.units_blk)('units') &
            pp.Optional(parameter.par_blk)('parameter') &
            pp.Optional(neuron.neuron_blk)('neuron') &
            pp.Optional(derivative.derivative_blk)('derivative') &
            pp.Optional(assigned.assigned_blk)('assigned') &
            pp.ZeroOrMore(pp.Group(procedure.procedure_blk)('procedures*')) &
            pp.ZeroOrMore(pp.Group(function.function_blk)('functions*')) &
            pp.Optional(breakpoint.breakpoint_blk)('breakpoint') &
            pp.Optional(state.state_blk)('state') &
            pp.Optional(initial.initial_blk)('initial')
            )
           .ignore(comment.comments)
           .ignore(terminals.UNITSOFF)
           .ignore(terminals.UNITSON)
           .ignore(terminals.THREADSAFE)).setParseAction(Program)


