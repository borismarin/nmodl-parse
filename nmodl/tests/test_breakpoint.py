from nmodl.breakpoint import solve, breakpoint_blk


def test_solve():
    assert(solve.parseString('SOLVE derivs').asList() ==
           ['SOLVE', 'derivs'])


def test_breakpoint():
    from textwrap import dedent
    test_string = dedent("""
    BREAKPOINT {
        SOLVE states
        ina = gnabar*m*h*(v - ena)
        ik = gkbar*n*(v - ek)
        il = gl*(v - el)
    }
    """)
    assert(breakpoint_blk.parseString(test_string).asList() ==
           ['BREAKPOINT',
               'SOLVE', 'states',
               'ina', 'gnabar', '*', 'm', '*', 'h', '*', ['v', '-', 'ena'],
               'ik', 'gkbar', '*', 'n', '*', ['v', '-', 'ek'],
               'il', 'gl', '*', ['v', '-', 'el'],
            ])
