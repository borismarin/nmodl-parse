class Node(object):

    def __init__(self, parsed):
        self.parsed = parsed
        self.unpack_parsed(parsed)

    def unpack_parsed(self):
        raise NotImplementedError
