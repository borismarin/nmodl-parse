import pyparsing as pp
from nmodl.terminals import STATE, LBRACE, RBRACE, ID
from units import unit_ref

state_var = ID('id') + pp.Optional(unit_ref)
state_blk = STATE - LBRACE + pp.ZeroOrMore(
    state_var('state_vars*')) + RBRACE
