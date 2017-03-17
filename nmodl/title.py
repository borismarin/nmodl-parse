import pyparsing as pp
from literals import TITLE

title = TITLE + pp.restOfLine().setWhitespaceChars(' \t')
