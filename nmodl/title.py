import pyparsing as pp
from nmodl.terminals import TITLE
from nmodl.node import Node


class Title(Node):
    def unpack_parsed(self, parsed):
        self.title = parsed.title

title = (TITLE + pp.restOfLine().setWhitespaceChars(' \t')('title')
         ).setParseAction(Title)
