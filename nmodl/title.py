import pyparsing as pp
from nmodl.literals import TITLE

title = TITLE + pp.restOfLine().setWhitespaceChars(' \t')
