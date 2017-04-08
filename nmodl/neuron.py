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


suffix_stmt = (SUFFIX + ID)
global_stmt = (GLOBAL + pp.Group(pp.delimitedList(ID)))
range_stmt = RANGE + pp.Group(pp.delimitedList(ID))
pointer_stmt = (POINTER + pp.Group(pp.delimitedList(ID)))
ext_stmt = (EXTERNAL + pp.Group(pp.delimitedList(ID)))
nonspec_stmt = (NONSPECIFIC + pp.Group(pp.delimitedList(ID)))

read = READ + pp.Group(pp.delimitedList(ID))('read')
write = WRITE + pp.Group(pp.delimitedList(ID))('write')
valence = VALENCE + FLOAT
rwv = pp.Optional(read) & pp.Optional(write) & pp.Optional(valence)
useion_stmt = (USEION + ID('ion') + rwv)

neuron_stmt = (suffix_stmt('suffix') | global_stmt | range_stmt | pointer_stmt
               | ext_stmt | nonspec_stmt | useion_stmt('use_ions*'))

neuron_blk = NEURON + LBRACE + pp.ZeroOrMore(neuron_stmt) + RBRACE
