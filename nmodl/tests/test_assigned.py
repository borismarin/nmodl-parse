from nmodl.assigned import assigned_blk


def test_assigned():
    from textwrap import dedent
    test_string = dedent("""
    ASSIGNED {
        v               (mV)
        celsius         (degC)
        ina             (mA/cm2)
        gna             (pS/um2)
        ena             (mV)
        minf            hinf
        mtau (ms)       htau (ms)
        tadj
    }

    """)
    assert(assigned_blk.parseString(test_string).asList() ==
           ['ASSIGNED',
               ['v', 'mV'],
               ['celsius', 'degC'],
               ['ina', 'mA/cm2'],
               ['gna', 'pS/um2'],
               ['ena', 'mV'],
               ['minf'],
               ['hinf'],
               ['mtau', 'ms'],
               ['htau', 'ms'],
               ['tadj'],

            ])
