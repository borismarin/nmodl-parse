from functools import singledispatch
from nmodl.program import Program
from nmodl.title import Title


@singledispatch
def unparse(obj):
    pass


@unparse.register(Program)
def _(program):
    return unparse(program.title[0]) 


@unparse.register(Title)
def _(title):
    return 'TITLE ' + title.title
