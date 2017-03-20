from pyparsing import Suppress, Keyword, Regex

LPAR = Suppress('(')
RPAR = Suppress(')')
LBRACK = Suppress('[')
RBRACK = Suppress(']')
LBRACE = Suppress('{')
RBRACE = Suppress('}')
COMMA = Suppress(',')

TITLE = Keyword('TITLE')
UNITS = Keyword('UNITS')
PARAMETER = Keyword('PARAMETER')
COMMENT = Keyword('COMMENT')
ASSIGNED = Keyword('ASSIGNED')
NEURON = Keyword('NEURON')

BREAKPOINT = Keyword('BREAKPOINT')
STATE = Keyword('STATE')
FUNCTION = Keyword('FUNCTION')
PROCEDURE = Keyword('PROCEDURE')
INITIAL = Keyword('INITIAL')
DERIVATIVE = Keyword('DERIVATIVE')

UNITSON = Keyword('UNITSON')
UNITSOFF = Keyword('UNITSOFF')
THREADSAFE = Keyword('THREADSAFE')

FLOAT = Regex('[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?')
