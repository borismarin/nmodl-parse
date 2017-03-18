from nmodl.parameter import par_def, par_blk


def test_par_decl():
    test_string = '(mV) = (millivolt)'
    assert(par_def.parseString(test_string).asList() ==
           [['mV', '=', 'millivolt']])


def test_none():
    test_string = 'PARAMETER { \n  }'
    assert(par_blk.parseString(test_string).asList() ==
           ['PARAMETER', []])


def test_two():
    from textwrap import dedent
    test_string = dedent("""
    PARAMTER {
        v (mV)
        celsius = 6.3 (degC)
    }
    """)
    assert(par_blk.parseString(test_string).asList() ==
           ['PARAMTER',
               ['v', '(mV)'],
               ['celsius', '=', '6.3', '(degC)']
            ])
