import pyparsing as pp

from nmodl.terminals import ID, INT, FLOAT

TABLE = pp.Keyword('TABLE')
WITH = pp.Keyword('WITH')
DEPEND = pp.Keyword('DEPEND')
FROM = pp.Keyword('FROM')
TO = pp.Keyword('TO')

ids = pp.delimitedList(ID)
arg = FLOAT | ID
iarg = INT | ID
table = TABLE + ids + DEPEND + ids + FROM + arg + TO + arg + WITH + iarg
