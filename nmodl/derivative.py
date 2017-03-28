import pyparsing as pp

from nmodl.terminals import DERIVATIVE, LBRACE, RBRACE, ID
from nmodl.expressions import body

derivative_blk = DERIVATIVE + ID + LBRACE + pp.Group(body) + RBRACE
