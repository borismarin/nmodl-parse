import pyparsing as pp
pp.ParserElement.enablePackrat()

from nmodl.terminals import FLOAT, ID, RBRACE, LBRACE, RPAR, LPAR, LOCAL, LBRACK, RBRACK
from nmodl.units import unit_ref
from nmodl.table import table


UNARY = pp.oneOf("! -")
MUL = pp.oneOf("* / %")
ADD = pp.oneOf("+ -")
POW = pp.Literal('^')
REL = pp.oneOf("< > <= >= == !=")
CON = pp.oneOf("&& ||")

IF = pp.Keyword('if')
WHILE = pp.Keyword('while')
ELSE = pp.Keyword('else')

expr = pp.Forward()
args = pp.Group(pp.Optional(pp.delimitedList(expr)))
func_call = ID + LPAR + args + RPAR
primed = pp.Combine(ID + pp.OneOrMore("'"))
operand = func_call | primed | ID | FLOAT + pp.Optional(unit_ref) 
expr << (pp.operatorPrecedence(operand,
                               [
                                   (pp.oneOf('! -'), 1, pp.opAssoc.RIGHT),
                                   (POW, 2, pp.opAssoc.RIGHT),
                                   (MUL, 2, pp.opAssoc.LEFT),
                                   (ADD, 2, pp.opAssoc.LEFT),
                                   (REL, 2, pp.opAssoc.LEFT),
                                   (CON, 2, pp.opAssoc.LEFT),
                                   (pp.Regex('(?<!=)=(?!=)'), 2, pp.opAssoc.LEFT),
                               ]) +
         pp.Optional(LBRACK + expr + RBRACK | LPAR + args + RPAR)
         )

local_var_def = LOCAL + pp.delimitedList(ID)
stmt = pp.Forward()

if_stmt = IF - LPAR + expr + RPAR + stmt + pp.Optional(ELSE + stmt)
while_stmt = WHILE - LPAR + expr + RPAR + stmt

stmt << (if_stmt |
         while_stmt |
         expr |
         LBRACE + pp.ZeroOrMore(stmt) + RBRACE)

vardecl = local_var_def


param = pp.Group(ID + pp.Optional(unit_ref))
body = pp.ZeroOrMore(vardecl) + pp.Optional(table) + pp.ZeroOrMore(stmt)
func_def = (ID + LPAR + pp.Optional(pp.Group(pp.delimitedList(param)))
           + RPAR + LBRACE + pp.Group(body) + RBRACE)
decl = func_def | vardecl

# set parser element names
for vname in ("if_stmt while_stmt args "
              "ID func_def vardecl param body stmt".split()):
    v = vars()[vname]
    v.setName(vname)
