import pyparsing as pp
from nmodl.terminals import PARAMETER, LBRACE, RBRACE, FLOAT, ID, LT, GT, COMMA
from nmodl.units import unit_ref

limit = LT + FLOAT + COMMA + FLOAT + GT
par_def = (ID
           + pp.Optional('=' + FLOAT)
           + pp.Optional(unit_ref)
           + pp.Optional(limit))
pars = pp.ZeroOrMore(pp.Group(par_def)('parameters*'))

par_blk = PARAMETER + LBRACE + pars + RBRACE
