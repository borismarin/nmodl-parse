import pyparsing as pp

# stolen from http://pyparsing.wikispaces.com/file/view/oc.py/150660287/oc.py

LPAR,RPAR,LBRACK,RBRACK,LBRACE,RBRACE,COMMA = map(pp.Suppress, "()[]{},")
INT = pp.Keyword("int")
WHILE = pp.Keyword("while")
IF = pp.Keyword("if")
ELSE = pp.Keyword("else")

NAME = pp.Word(pp.alphas+"_", pp.alphanums+"_")
integer = pp.Regex(r"[+-]?\d+")

expr = pp.Forward()
operand = NAME | integer 
expr << (pp.operatorPrecedence(operand, 
    [
    (pp.oneOf('! - *'), 1, pp.opAssoc.RIGHT),
    (pp.oneOf('* / %'), 2, pp.opAssoc.LEFT),
    (pp.oneOf('+ -'), 2, pp.opAssoc.LEFT),
    (pp.oneOf('< == > <= >= !='), 2, pp.opAssoc.LEFT),
    (pp.Regex(r'=[^=]'), 2, pp.opAssoc.LEFT),
    ]) + 
    pp.Optional( LBRACK + expr + RBRACK | 
              LPAR + pp.Group(pp.Optional(pp.delimitedList(expr))) + RPAR )
    )

stmt = pp.Forward()

ifstmt = IF - LPAR + expr + RPAR + stmt + pp.Optional(ELSE + stmt)
whilestmt = WHILE - LPAR + expr + RPAR + stmt

stmt << pp.Group( ifstmt |
          whilestmt |
          expr |
          LBRACE + pp.ZeroOrMore(stmt) + RBRACE)

vardecl = pp.Group(NAME + pp.Optional(LBRACK + integer + RBRACK))

arg = pp.Group(NAME)
body = pp.ZeroOrMore(vardecl) + pp.ZeroOrMore(stmt)
fundecl = pp.Group(NAME + LPAR + pp.Optional(pp.Group(pp.delimitedList(arg))) + RPAR +
            LBRACE + pp.Group(body) + RBRACE)


for vname in ("ifstmt whilestmt "
               "NAME fundecl vardecl arg body stmt".split()):
    v = vars()[vname]
    v.setName(vname)

#for vname in "fundecl stmt".split():
#    v = vars()[vname]
#    v.setDebug()

def parse_print(node, code_str):
    ast = node.parseString(code_str, parseAll=True)

    import pprint
    pprint.pprint(ast.asList())

parse_print(expr, '''
a = 10
''')

parse_print(ifstmt, '''
if(1+1 == 2) 1
else  0
''')

parse_print(pp.ZeroOrMore(stmt), '''
a = 1
a + 1
if(a == 12){
1 + 1
2 % 21}
else 
sin(x)
''')

parse_print(fundecl, '''
funfun(ab, c){
    1+2
    if(c == 2){
    42
}
}
''')