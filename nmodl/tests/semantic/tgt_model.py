from __future__ import division
from math import exp, fabs


class NModlMechanism(object):
    pass


class _ik(NModlMechanism):

    def __init__(self):
        self.gkbar = 0.036

    def initial(self, external):
        v = external['v']
        return {
            'n': self.alpha(v)/(self.alpha(v) + self.beta(v))
        }

    def alpha(self, v):
        x = (v + 55) / 10
        if(fabs(x) > 1e-6):
            alpha = 0.1*x/(1-exp(-x))
        else:
            alpha = 0.1/(1-0.5*x)
        return alpha

    def beta(self, v):
        return 0.125 * exp(-(v + 65) / 80)

    def derivative(self, external):
        v = external['v']
        n = external['n']
        return {'n':
                (1 - n) * self.alpha(v) - n * self.beta(v)
                }

    def ik(self, external):  # do we get one method for each WRITE?
        n = external['n']
        v = external['v']
        ek = external['ek']
        return self.gkbar * n ** 4 * (v - ek)


def test_metavisit():
    import ast

    class allnames(ast.NodeVisitor):
        def visit_Module(self, node):
            self.names = set()
            self.generic_visit(node)
            print(sorted(self.names))

        def visit_Name(self, node):
            self.names.add(node.id)

    allnames().visit(ast.parse(open(__file__).read()))
