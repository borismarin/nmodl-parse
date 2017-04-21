from functools import singledispatch
from nmodl.expressions import (Assignment, Binary, Primed, FuncCall, Unary) 

@singledispatch
def genlems(x, visitor):
    1/0
    pass


@genlems.register(Binary)
def _(a, visitor):
    return '{} {} {}'.format(genlems(a.left, visitor), a.op, genlems(a.right,
                                                                     visitor))


@genlems.register(Assignment)
def _(a, visitor):
    return '{} {} {}'.format(genlems(a.left, visitor), a.op, genlems(a.right,
                                                                     visitor))


@genlems.register(Primed)
def _(p, visitor):
    return genlems(p.variable, visitor) + "'"


@genlems.register(FuncCall)
def _(f, visitor):
    try:
        print(visitor.functions)
        fd = visitor.functions.get(f.func)
        print('found func', f.func, fd)
    except:
        pass
    1/0
    arglist = ', '.join([genlems(arg, visitor) for arg in f.args])
    return f.func + '(' + arglist + ')'


@genlems.register(Unary)
def _(u, visitor):
    return u.op + genlems(u.operand, visitor)



@genlems.register(str)
def _(s, visitor):
    return s


