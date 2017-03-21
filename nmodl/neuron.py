import pyparsing as pp
from nmodl.terminals import NEURON, LBRACE, RBRACE, FLOAT

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

id = pp.Word(pp.alphas, pp.alphanums+'_')  # TODO: allowed ids?

suffix_stmt = (SUFFIX + id)
global_stmt = (GLOBAL + pp.Group(pp.delimitedList(id)))
range_stmt = RANGE + pp.Group(pp.delimitedList(id))
pointer_stmt = (POINTER + pp.Group(pp.delimitedList(id)))
ext_stmt = (EXTERNAL + pp.Group(pp.delimitedList(id)))
nonspec_stmt = (NONSPECIFIC + pp.Group(pp.delimitedList(id)))

read = READ + pp.Group(pp.delimitedList(id))
write = WRITE + pp.Group(pp.delimitedList(id))
valence = VALENCE + FLOAT
rwv = pp.Optional(read) & pp.Optional(write) & pp.Optional(valence)
useion_stmt = (USEION + id + rwv)

neuron_stmt = pp.Group(suffix_stmt | global_stmt | range_stmt | pointer_stmt |
               ext_stmt | nonspec_stmt | useion_stmt)

neuron_blk = NEURON + LBRACE + pp.ZeroOrMore(neuron_stmt) + RBRACE
