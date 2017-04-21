import pyparsing as pp

from nmodl.terminals import (FLOAT, ID, RBRACE, LBRACE, RPAR, LPAR, LOCAL,
                             LBRACK, RBRACK)
from nmodl.units import unit_ref
from nmodl.table import table

pp.ParserElement.enablePackrat()


class Statement(object):
    pass


class Expression(Statement):
    pass


class Unary(object):
    def __init__(self, unary):
        self.op, self.operand = unary[0]


class Binary(Expression):
    def __init__(self, bin):
        self.left, self.op, self.right = bin[0]
    def __repr__(self):
        return repr([self.left, self.op, self.right])
    def __str__(self):
        return '{} {} {}'.format(str(self.left), self.op, str(self.right))


class Assignment(Binary):
    pass


class FuncCall(object):
    def __init__(self, fc):
        self.func = fc.func
        self.args = fc.args.asList()

    def __repr__(self):
        return repr([self.func, self.args])

    def __str__(self):
        return self.func + '(' + str(self.args) + ')'

class FuncDef(object):
    def __init__(self, fd):
        self.name = fd.fname
        self.args = fd.args.asList()
        self.unit = fd.unit
        self.body = fd.body

    def __repr__(self):
        return 'function ' + self.name + '(' + str(self.args) + ')'

    def __str__(self):
        return 'function ' + self.name + '(' + str(self.args) + ')'


class Addition(Binary):
    pass


class IfStatement(Statement):
    pass


class WhileStatement(Statement):
    pass


class Primed(object):
    def __init__(self, p):
        self.variable = p.id
    def __repr__(self):
        return self.variable+"'"
    def __str__(self):
        return self.variable+"'"


#class Identifier(object):
#    def __init__(self, v):
#        self.id = v.id
#    def __str__(self):
#        return self.id
#    def __repr__(self):
#        return self.id

#ID.setParseAction(Identifier)

UNARY = pp.oneOf("! -")
MUL = pp.oneOf("* / %")
ADD = pp.oneOf("+ -")
POW = pp.Literal('^')
REL = pp.oneOf("< > <= >= == !=")
CON = pp.oneOf("&& ||")
ASSIGN = pp.Regex('(?<!=)=(?!=)')

IF = pp.Keyword('if')
WHILE = pp.Keyword('while')
ELSE = pp.Keyword('else')

expr = pp.Forward()
args = pp.Optional(pp.delimitedList(expr))
func_call = ID('func') + LPAR + args('args') + RPAR
primed = pp.Combine(ID + pp.OneOrMore("'")).setParseAction(Primed)
operand = func_call.setParseAction(FuncCall) | primed | ID | (FLOAT + pp.Optional(unit_ref))
expr <<= (pp.infixNotation(operand,
       [
           (UNARY, 1, pp.opAssoc.RIGHT, Unary),
           (POW, 2, pp.opAssoc.RIGHT),
           (MUL, 2, pp.opAssoc.LEFT),
           (ADD, 2, pp.opAssoc.LEFT, Addition),
           (REL, 2, pp.opAssoc.LEFT),
           (CON, 2, pp.opAssoc.LEFT),
           (ASSIGN, 2, pp.opAssoc.LEFT, Assignment)
        ]) +
         pp.Optional(LBRACK + expr + RBRACK | LPAR + args + RPAR)
         )

stmt = pp.Forward()

if_stmt = IF - LPAR + expr + RPAR + stmt + pp.Optional(ELSE + stmt)
while_stmt = WHILE - LPAR + expr + RPAR + stmt

stmt << (if_stmt.setParseAction(IfStatement) |
         while_stmt.setParseAction(WhileStatement) |
         expr |
         LBRACE + pp.ZeroOrMore(stmt) + RBRACE)

vardecl = LOCAL + pp.delimitedList(ID)

param = ID + pp.Optional(unit_ref)
body = pp.ZeroOrMore(vardecl) & pp.Optional(table) & pp.ZeroOrMore(stmt)
func_def = (ID('fname') + LPAR + pp.Optional(pp.delimitedList(param)('args*')) + RPAR + pp.Optional(unit_ref)('unit') + LBRACE + body('body') + RBRACE).setParseAction(FuncDef)
decl = func_def | vardecl
