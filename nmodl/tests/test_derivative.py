from textwrap import dedent

from nmodl.derivative import derivative_blk
from nmodl.expressions import primed


def test_prime():
    assert(primed.parseString("x''").asList() == ["x''"])


def test_deriv():
    blk = dedent("""
    DERIVATIVE states {
        trates(v+vshift)
        m' =  (minf-m)/mtau
        h' =  (hinf-h)/htau
        x''' = y + 3*x''*y' + sin(x')
        }
    """)
    assert(derivative_blk.parseString(blk).asList() ==
           ['DERIVATIVE', 'states',
            ['trates', [['v', '+', 'vshift']],
             ["m'", '=', [['minf', '-', 'm'], '/', 'mtau']],
             ["h'", '=', [['hinf', '-', 'h'], '/', 'htau']],
             ["x'''", '=', ['y', '+', ['3', '*', "x''", '*', "y'"], '+', 'sin', ["x'"]]]
             ]])
