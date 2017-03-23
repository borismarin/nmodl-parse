import pyparsing as pp
from nmodl.terminals import PARAMETER, LBRACE, RBRACE, FLOAT, ID
from nmodl.units import unit_ref

par_def = ID + pp.Optional('=' + FLOAT) + pp.Optional(unit_ref)
pars = pp.OneOrMore(pp.Group(par_def))

par_blk = PARAMETER + LBRACE + pp.Optional(pars, default=[]) + RBRACE
