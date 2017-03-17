import pyparsing as pp
from nmodl.literals import UNITS, LBRACE, RBRACE, LPAR, RPAR

id = pp.Word(pp.alphanums + '/')

pid = LPAR + id + RPAR
unit = pp.Group(pid + '=' + pid)

units = pp.OneOrMore(unit)
units_blk = UNITS + LBRACE + pp.Optional(units, default=[]) + RBRACE

