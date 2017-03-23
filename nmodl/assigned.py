import pyparsing as pp
from nmodl.terminals import ASSIGNED, LBRACE, RBRACE, ID
from nmodl.units import unit_ref


assigned_def = ID + pp.Optional(unit_ref)
assigneds = pp.OneOrMore(pp.Group(assigned_def))

assigned_blk = ASSIGNED + LBRACE + pp.Optional(assigneds, default=[]) + RBRACE
