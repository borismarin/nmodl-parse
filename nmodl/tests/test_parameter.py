from nmodl.parameter import par_def, par_blk


def test_par_decl():
    test_string = 'erev = -70      (mV) '
    assert(par_def.parseString(test_string).asList() ==
           ['erev', '=', '-70', 'mV'])

def test_limits():
    test_string = 'erev = -70      (mV) <-1e2, 0.1e3>'
    assert(par_def.parseString(test_string).asList() ==
           ['erev', '=', '-70', 'mV', '-1e2', '0.1e3'])


def test_none():
    test_string = 'PARAMETER { \n  }'
    assert(par_blk.parseString(test_string).asList() ==
           ['PARAMETER'])


def test_two():
    from textwrap import dedent
    test_string = dedent("""
    PARAMETER {
        v (mV)
        celsius = 6.3 (degC)
    }
    """)
    assert(par_blk.parseString(test_string).asList() ==
           ['PARAMETER',
               ['v', 'mV'],
               ['celsius', '=', '6.3', 'degC']
            ])
