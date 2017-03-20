import pyparsing as pp
from nmodl.terminals import ASSIGNED, LBRACE, RBRACE
from nmodl.units import unit_ref

id = pp.Word(pp.alphas, pp.alphanums+'_')  # TODO: allowed ids?

assigned_def = id + pp.Optional(unit_ref)
assigneds = pp.OneOrMore(pp.Group(assigned_def))

assigned_blk = ASSIGNED + LBRACE + pp.Optional(assigneds, default=[]) + RBRACE
