import pyparsing as pp
from nmodl.terminals import ASSIGNED, LBRACE, RBRACE, ID
from nmodl.units import unit_ref


assigned_def = ID + pp.Optional(unit_ref)
assigneds = pp.ZeroOrMore(pp.Group(assigned_def)('assigneds*'))

assigned_blk = ASSIGNED + LBRACE + assigneds + RBRACE
