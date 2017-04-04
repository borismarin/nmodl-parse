import pyparsing as pp
from nmodl.terminals import STATE, LBRACE, RBRACE, ID

state_blk = STATE - LBRACE + pp.Group(pp.OneOrMore(ID))('state_vars') + RBRACE
