import pyparsing as pp

from nmodl import (assigned, breakpoint, title, parameter, units, procedure,
                   function, state, comment, terminals, initial)

program = ((pp.Optional(title.title)('title') &
            pp.Optional(units.units_blk)('units') &
            pp.Optional(parameter.par_blk)('parameter') &
            pp.Optional(assigned.assigned_blk)('assigned') &
            pp.Optional(procedure.procedure_blk)('procedure') &
            pp.Optional(function.function_blk)('function') &
            pp.Optional(breakpoint.breakpoint_blk)('breakpoint') &
            pp.Optional(state.state_blk)('state') &
            pp.Optional(initial.initial_blk)('initial')
            )
           .ignore(comment.comments)
           .ignore(terminals.UNITSOFF)
           .ignore(terminals.UNITSON)
           .ignore(terminals.THREADSAFE))
