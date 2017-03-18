import pyparsing as pp

from nmodl import title, units, parameter

program = (pp.Optional(title.title)('title') &
           pp.Optional(units.units_blk)('units') &
           pp.Optional(parameter.par_blk)('parameter'))
