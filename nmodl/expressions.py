import pyparsing as pp
from nmodl.terminals import FLOAT, ID, RBRACE, LBRACE, RPAR, LPAR, LOCAL
from nmodl.units import unit_ref

# adapted from http://pyparsing.wikispaces.com/file/view/pymicko.py

MUL = pp.oneOf("* /")
ADD = pp.oneOf("+ -")
RELATIONAL_OPERATORS = pp.oneOf("< > <= >= == !=")

Exp = pp.Forward()
MulExp = pp.Forward()
NumExp = pp.Forward()
Arguments = pp.delimitedList(NumExp("exp") + pp.Optional(unit_ref))
FunctionCall = ID + pp.FollowedBy('(') + \
    LPAR + pp.Optional(Arguments)("args") + RPAR

Exp << (FunctionCall
        | FLOAT
        | ID
        | pp.Group(LPAR + NumExp + RPAR)
        | pp.Group("+" + Exp)
        | pp.Group("-" + Exp))
MulExp << (Exp + pp.ZeroOrMore(MUL + Exp))
NumExp << (MulExp + pp.ZeroOrMore(ADD + MulExp))

AndExp = pp.Forward()
LogExp = pp.Forward()
RelExp = (NumExp + RELATIONAL_OPERATORS + NumExp)
AndExp << RelExp("exp") + pp.ZeroOrMore(pp.Literal("&&") + RelExp("exp"))
LogExp << AndExp("exp") + pp.ZeroOrMore(pp.Literal("||") + AndExp("exp"))

Statement = pp.Forward()
StatementList = pp.Forward()
AssignmentStatement = (ID + pp.Suppress("=") + NumExp("exp"))
FunctionCallStatement = FunctionCall

IfStatement = ((pp.Keyword("if") + pp.FollowedBy("(")) +
               (LPAR + LogExp + RPAR) +
               (Statement + pp.Empty()) +
               pp.Optional(pp.Keyword("else") + Statement))
WhileStatement = ((pp.Keyword("while") + pp.FollowedBy("(")) +
                  (LPAR + LogExp + RPAR) + Statement)
CompoundStatement = pp.Group(LBRACE + StatementList + RBRACE)
Statement << (IfStatement | WhileStatement |
              FunctionCallStatement | AssignmentStatement | CompoundStatement)
StatementList << pp.ZeroOrMore(Statement)

LocalVariable = LOCAL + ID
LocalVariableList = pp.ZeroOrMore(LocalVariable)

FunctionBody = LBRACE + pp.Optional(LocalVariableList) \
    + StatementList + RBRACE
Parameter = ID
ParameterList = pp.delimitedList(Parameter)
Function = ID + pp.Group(LPAR + pp.Optional(ParameterList)("params")
                         + RPAR + FunctionBody)
