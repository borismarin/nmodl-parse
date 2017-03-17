import pyparsing as pp
from nmodl.terminals import TITLE

title = TITLE + pp.restOfLine().setWhitespaceChars(' \t')
