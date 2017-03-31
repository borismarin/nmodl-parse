import pyparsing as pp

from nmodl import (assigned, breakpoint, title, parameter, units, procedure,
                   function, state, comment, terminals, initial, neuron,
                   derivative)


class Program(object):
    def __init__(self, t):
        self.title = t.title

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


