import pyparsing as pp

from nmodl.terminals import BREAKPOINT, LBRACE, RBRACE, ID
from nmodl.expressions import stmts

solve = pp.Keyword('SOLVE') + ID + pp.Optional(pp.Keyword('METHOD') + ID)
breakpoint_blk = BREAKPOINT + LBRACE +\
    (pp.Optional(solve) & stmts) + RBRACE
