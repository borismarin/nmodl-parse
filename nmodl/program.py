import pyparsing as pp

from nmodl import title, units, parameter, comment, assigned, terminals

program = (pp.Optional(title.title)('title') &
           pp.Optional(units.units_blk)('units') &
           pp.Optional(parameter.par_blk)('parameter') &
           pp.Optional(assigned.assigned_blk)('assigned')
           ).ignore(comment.comments)\
            .ignore(terminals.UNITSOFF)\
            .ignore(terminals.UNITSON)\
            .ignore(terminals.THREADSAFE)
