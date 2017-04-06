from math import exp, fabs


class NModlMechanism(object):
    pass


class _ik(NModlMechanism):
    gkbar = 0.036
    n = None
    v = None

    @property
    def state(self):
        return {'n': self.n, 'v': self.v}

    @property
    def parameters(self):
        return {'gkbar': self.gkbar}

    def __init__(self, v0):  # need v from outside world...
        x0 = self.initial(v0)
        for xn, xv in x0.iteritems:
            self.state[xn] = xv

    def initial(self, v0):
        return {
            'n': self.alpha(self.v)/(self.alpha(self.v) - self.beta(self.v)),
            'v': v0
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

    def derivative(self):
        return {'n':
                (1 - self.n) * self.alpha(self.v) - self.n * self.beta(self.v)
                }


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
