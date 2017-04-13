import nmodl.neuron as n


def test_global():
    # RANGE, POINTER, NONSPECIFIC, EXTERNAL are identical
    test_string = 'GLOBAL minf'
    p = n.global_stmt.parseString(test_string)
    assert(p.globals.asList() == ['minf'])

    test_string = 'GLOBAL minf, hinf'
    p = n.global_stmt.parseString(test_string)
    assert(p.globals.asList() == ['minf', 'hinf'])


def test_suffix():
    test_string = 'SUFFIX xyz'
    assert(n.suffix_stmt.parseString(test_string).asList() ==
           ['SUFFIX', 'xyz'])


def test_useion():
    test_string = 'USEION ca'
    assert(n.useion_stmt.parseString(test_string).asList() ==
           ['USEION', 'ca'])

    test_string = 'USEION na READ ena'
    assert(n.useion_stmt.parseString(test_string).asList() ==
           ['USEION', 'na', 'READ', 'ena'])

    test_string = 'USEION na WRITE ina'
    assert(n.useion_stmt.parseString(test_string).asList() ==
           ['USEION', 'na', 'WRITE', 'ina'])

    test_string = 'USEION na WRITE ina READ ena'
    assert(n.useion_stmt.parseString(test_string).asList() ==
           ['USEION', 'na', 'WRITE', 'ina', 'READ', 'ena'])

    test_string = 'USEION na WRITE ina, ki READ ena VALENCE +1'
    assert(n.useion_stmt.parseString(test_string).asList() ==
           ['USEION', 'na', 'WRITE', 'ina', 'ki',
            'READ', 'ena', 'VALENCE', '+1'])


def test_neuron():
    from textwrap import dedent
    test_string = dedent("""
    NEURON {
        GLOBAL x
        USEION na READ ena WRITE ina
        USEION k READ ek WRITE ik VALENCE +1
        NONSPECIFIC_CURRENT il
        RANGE gnabar, gkbar, gl, el
        SUFFIX hh1
        GLOBAL minf, hinf, ninf, mexp, hexp, nexp
    }
    """)
    assert(n.neuron_blk.parseString(test_string).asList() ==
           ['NEURON',
            'GLOBAL', 'x',
            'USEION', 'na', 'READ', 'ena', 'WRITE', 'ina',
            'USEION', 'k', 'READ', 'ek', 'WRITE', 'ik', 'VALENCE', '+1',
            'NONSPECIFIC_CURRENT', 'il',
            'RANGE', 'gnabar', 'gkbar', 'gl', 'el',
            'SUFFIX', 'hh1',
            'GLOBAL', 'minf', 'hinf', 'ninf', 'mexp', 'hexp', 'nexp'
            ])


def test_naming():
    from textwrap import dedent
    test_string = dedent("""
    NEURON {
        GLOBAL x
        USEION na READ ena WRITE ina
        USEION k READ ek WRITE ik VALENCE +1
        NONSPECIFIC_CURRENT il
        RANGE gnabar, gkbar, gl, el
        SUFFIX hh1
        USEION ca READ cao, cai WRITE cai, ica
        GLOBAL minf, hinf, ninf, mexp, hexp, nexp
    }
    """)
    parsed = n.neuron_blk.parseString(test_string)
    assert(parsed.suffix == 'hh1')
    assert(parsed.use_ions[0].ion == 'na')
    assert(parsed.use_ions[1].reads.asList() == ['ek'])
    assert(parsed.use_ions[2].writes.asList() == ['cai', 'ica'])
