import pyparsing as pp
from nmodl.terminals import STATE, LBRACE, RBRACE

id = pp.Word(pp.alphas, pp.alphanums+'_')  # TODO: allowed ids?
state_blk = STATE - LBRACE + pp.Group(pp.OneOrMore(id)) + RBRACE
