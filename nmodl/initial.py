from nmodl.terminals import INITIAL, LBRACE, RBRACE
from nmodl.expressions import body

initial_blk = INITIAL + LBRACE + body + RBRACE
