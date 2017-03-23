import pyparsing as pp
from nmodl.terminals import (FLOAT, ID, RBRACE,
                             LBRACE, RBRACK, LBRACK, RPAR, LPAR)

# stolen from http://pyparsing.wikispaces.com/file/view/oc.py/150660287/oc.py
#  submitting a PR with the better regexp for assignents (L24) would be kind

WHILE = pp.Keyword("while")
IF = pp.Keyword("if")
ELSE = pp.Keyword("else")

INT = pp.Regex(r"[+-]?\d+")


expr = pp.Forward()
operand = ID | FLOAT
expr << (pp.operatorPrecedence(
    operand,
    [
        (pp.oneOf('! - *'), 1, pp.opAssoc.RIGHT),
        (pp.oneOf('* / %'), 2, pp.opAssoc.LEFT),
        (pp.oneOf('+ -'), 2, pp.opAssoc.LEFT),
        (pp.oneOf('< == > <= >= !='), 2, pp.opAssoc.LEFT),
        (pp.Regex('(?<!=)=(?!=)'), 2, pp.opAssoc.LEFT),  # corected original 
    ]) +
    pp.Optional(LBRACK + expr + RBRACK |
                LPAR + pp.Group(pp.Optional(pp.delimitedList(expr))) + RPAR)
    )

stmt = pp.Forward()

ifstmt = IF - LPAR + expr + RPAR + stmt + pp.Optional(ELSE + stmt)
whilestmt = WHILE - LPAR + expr + RPAR + stmt

stmt << pp.Group(ifstmt |
                 whilestmt |
                 expr |
                 LBRACE + pp.ZeroOrMore(stmt) + RBRACE)

vardecl = pp.Group(ID + pp.Optional(LBRACK + INT + RBRACK))

body = pp.ZeroOrMore(stmt)

#arg = pp.Group(ID)
##body = pp.ZeroOrMore(vardecl) + pp.ZeroOrMore(stmt)
##fundecl = pp.Group(ID + LPAR + pp.Optional(pp.Group(pp.delimitedList(arg)))
#                   + RPAR + LBRACE + pp.Group(body) + RBRACE)


for vname in ("ifstmt whilestmt ID vardecl stmt".split()):
    v = vars()[vname]
    v.setName(vname)

# for vname in "fundecl stmt".split():
#     v = vars()[vname]
#     v.setDebug()