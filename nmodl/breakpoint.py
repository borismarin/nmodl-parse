import pyparsing as pp

from nmodl.terminals import BREAKPOINT, LBRACE, RBRACE, ID
from nmodl.expressions import stmts

SOLVE = pp.Keyword('SOLVE')
solve = SOLVE + ID
breakpoint_blk = BREAKPOINT + LBRACE +\
    (pp.Optional(solve) & stmts) + RBRACE
