import pyparsing as pp


LPAR = pp.Suppress('(')
RPAR = pp.Suppress(')')
LBRACK = pp.Suppress('[')
RBRACK = pp.Suppress(']')
LBRACE = pp.Suppress('{')
RBRACE = pp.Suppress('}')
COMMA = pp.Suppress(',')
LT = pp.Suppress('<')
GT = pp.Suppress('>')

TITLE = pp.Keyword('TITLE')
UNITS = pp.Keyword('UNITS')
PARAMETER = pp.Keyword('PARAMETER')
COMMENT = pp.Keyword('COMMENT')
ASSIGNED = pp.Keyword('ASSIGNED')
NEURON = pp.Keyword('NEURON')
BREAKPOINT = pp.Keyword('BREAKPOINT')
STATE = pp.Keyword('STATE')
FUNCTION = pp.Keyword('FUNCTION')
PROCEDURE = pp.Keyword('PROCEDURE')
INITIAL = pp.Keyword('INITIAL')
DERIVATIVE = pp.Keyword('DERIVATIVE')
LOCAL = pp.Keyword('LOCAL')

UNITSON = pp.Keyword('UNITSON')
UNITSOFF = pp.Keyword('UNITSOFF')
THREADSAFE = pp.Keyword('THREADSAFE')

FLOAT = pp.Regex('[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?')('float_literal')
INT = pp.Word(pp.nums)

ID = pp.Word(pp.alphas, pp.alphanums+'_')('id')  # TODO: allowed ids?
