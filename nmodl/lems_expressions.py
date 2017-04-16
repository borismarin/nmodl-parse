from functools import singledispatch
from nmodl.expressions import (Assignment, Binary, Primed, FuncCall, Unary,
                               Identifier)


@singledispatch
def genlems(x):
    1/0
    pass


@genlems.register(Binary)
def _(a):
    return genlems(a.left), a.op, genlems(a.right)


@genlems.register(Assignment)
def _(a):
    return genlems(a.left), a.op, genlems(a.right)


@genlems.register(Primed)
def _(p):
    return genlems(p.variable) + "'"


@genlems.register(FuncCall)
def _(f):
    return f.func + '(' + genlems(f.args) + ')'


@genlems.register(Unary)
def _(u):
    return u.op + genlems(u.operand)


@genlems.register(Identifier)
def _(i):
    return i.id

@genlems.register(str)
def _(s):
    return s


