import pyparsing as pp
from nmodl.terminals import PARAMETER, LBRACE, RBRACE, FLOAT
from nmodl.units import unit_ref

par_id = pp.Word(pp.alphas, pp.alphanums+'_')  # TODO: allowed ids?
par_decl = par_id

par_def = par_id + pp.Optional('=' + FLOAT) + pp.Optional(unit_ref)
pars = pp.OneOrMore(pp.Group(par_def))

par_blk = PARAMETER + LBRACE + pp.Optional(pars, default=[]) + RBRACE
