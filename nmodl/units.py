import pyparsing as pp
from nmodl.terminals import UNITS, LBRACE, RBRACE, LPAR, RPAR

unit_id = pp.Word(pp.alphanums + '/')  # TODO: allowed units?

unit_ref = LPAR + unit_id + RPAR
unit_def = pp.Group(unit_ref + '=' + unit_ref)

units = pp.OneOrMore(unit_def)
units_blk = UNITS + LBRACE + pp.Optional(units, default=[]) + RBRACE
