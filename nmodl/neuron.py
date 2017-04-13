import pyparsing as pp
from nmodl.terminals import NEURON, LBRACE, RBRACE, FLOAT, ID

SUFFIX = pp.Keyword('SUFFIX')
USEION = pp.Keyword('USEION')
READ = pp.Keyword('READ')
WRITE = pp.Keyword('WRITE')
RANGE = pp.Keyword('RANGE')
GLOBAL = pp.Keyword('GLOBAL')
POINTER = pp.Keyword('POINTER')
NONSPECIFIC = pp.Keyword('NONSPECIFIC_CURRENT')
EXTERNAL = pp.Keyword('EXTERNAL')
VALENCE = pp.Keyword('VALENCE')


suffix_stmt = SUFFIX + ID('suffix')
global_stmt = GLOBAL + pp.delimitedList(ID)('globals')
range_stmt = RANGE + pp.delimitedList(ID)('ranges')
pointer_stmt = POINTER + pp.delimitedList(ID)('pointers')
ext_stmt = EXTERNAL + pp.delimitedList(ID)('externals')
nonspec_stmt = NONSPECIFIC + pp.delimitedList(ID)('nonspecifics')

read = READ + pp.delimitedList(ID)('reads')
write = WRITE + pp.delimitedList(ID)('writes')
valence = VALENCE + FLOAT
rwv = pp.Optional(read) & pp.Optional(write) & pp.Optional(valence)
useion_stmt = USEION + ID('ion') + rwv

neuron_stmt = (suffix_stmt | global_stmt | range_stmt | pointer_stmt
               | ext_stmt | nonspec_stmt | useion_stmt('use_ions*'))

neuron_blk = NEURON + LBRACE + pp.ZeroOrMore(neuron_stmt) + RBRACE
