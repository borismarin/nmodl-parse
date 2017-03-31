import pyparsing as pp
from nmodl.terminals import UNITS, LBRACE, RBRACE, LPAR, RPAR
from nmodl.node import Node


class Units(Node):
    def unpack_parsed(self, parsed):
        self.unit_defs = [ud[0] for ud in parsed.unit_defs]


class UnitDef(Node):
    def unpack_parsed(self, parsed):
        # TODO: validation here or in visitor?
        self.left = parsed[0][0]
        self.right = parsed[0][-1]


class UnitRef(Node):
    def unpack_parsed(self, parsed):
        self.id = parsed[0]


unit_id = pp.Word(pp.alphanums + '/')

unit_ref = (LPAR + unit_id + RPAR).setParseAction(UnitRef)
unit_def = pp.Group(unit_ref + '=' + unit_ref).setParseAction(UnitDef)

units_blk = (UNITS + LBRACE +
             pp.ZeroOrMore(pp.Group(unit_def)('unit_defs*')) +
             RBRACE).setParseAction(Units)
