import pyparsing as pp
from nmodl.terminals import FLOAT, ID, RBRACE, LBRACE, RPAR, LPAR, LOCAL
from nmodl.units import unit_ref

# adapted from http://pyparsing.wikispaces.com/file/view/pymicko.py

MUL = pp.oneOf("* /")
ADD = pp.oneOf("+ -")
RELATIONAL_OPERATORS = pp.oneOf("< > <= >= == !=")

expr = pp.Forward()
mult_expr = pp.Forward()
num_expr = pp.Forward()
arguments = pp.delimitedList(num_expr("exp"))
func_call = ID + pp.FollowedBy('(') + \
    LPAR + pp.Optional(arguments)("args") + RPAR

expr << (func_call
         | FLOAT
         | ID
         | pp.Group(LPAR + num_expr + RPAR)
         | pp.Group("+" + expr)
         | pp.Group("-" + expr))
mult_expr << (expr + pp.ZeroOrMore(MUL + expr))
num_expr << (mult_expr + pp.ZeroOrMore(ADD + mult_expr))

and_expr = pp.Forward()
logic_expr = pp.Forward()
rel_expr = (num_expr + RELATIONAL_OPERATORS + num_expr)
and_expr << rel_expr("exp") + pp.ZeroOrMore(pp.Literal("&&") + rel_expr("exp"))
logic_expr << and_expr(
    "exp") + pp.ZeroOrMore(pp.Literal("||") + and_expr("exp"))

stmt = pp.Forward()
stmts = pp.Forward()
assignment = (ID + pp.Suppress("=") + num_expr("exp"))
call_stmt = func_call

if_stmt = ((pp.Keyword("if") + pp.FollowedBy("(")) +
           (LPAR + logic_expr + RPAR) +
           (stmt + pp.Empty()) +
           pp.Optional(pp.Keyword("else") + stmt))
while_stmt = ((pp.Keyword("while") + pp.FollowedBy("(")) +
              (LPAR + logic_expr + RPAR) + stmt)
compound_stmt = pp.Group(LBRACE + stmts + RBRACE)
stmt << (if_stmt | while_stmt | call_stmt | assignment | compound_stmt)
stmts << pp.ZeroOrMore(stmt)

local_var_def = LOCAL + pp.delimitedList(ID)
local_var_defs = pp.ZeroOrMore(local_var_def)

func_body = LBRACE + pp.Optional(local_var_defs) \
    + stmts + RBRACE
func_par = ID + pp.Optional(unit_ref)
func_pars = pp.delimitedList(func_par)
func_def = ID + \
    pp.Group(LPAR + pp.Optional(func_pars("params")) + RPAR + func_body)
