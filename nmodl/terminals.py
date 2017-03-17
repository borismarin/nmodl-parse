from pyparsing import Suppress, Keyword, Regex

LPAR = Suppress('(')
RPAR = Suppress(')')
LBRACK = Suppress('[')
RBRACK = Suppress(']')
LBRACE = Suppress('{')
RBRACE = Suppress('}')
SEMI = Suppress(';')
COMMA = Suppress(',')

TITLE = Keyword('TITLE')
UNITS = Keyword('UNITS')
NEURON = Keyword('NEURON')
PARAMETER = Keyword('PARAMETER')
ASSIGNED = Keyword('ASSIGNED')
BREAKPOINT = Keyword('BREAKPOINT')
COMMENT = Keyword('COMMENT')

FLOAT = Regex('[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?')
