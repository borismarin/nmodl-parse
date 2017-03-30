import os
from nmodl.program import program


def get_sample(fname):
    return os.path.join(os.path.dirname(__file__), 'sample_mods', fname)


def test_passive():
    parsed = program.parseFile(get_sample('passiv.mod'))
    #  to be improved
    #  passive.mod has UNITS, NEURON, PARAMETER, ASSIGNED, BREAKPOINT
    assert(len(parsed.asDict()) == 6)


def test_leak():
    parsed = program.parseFile(get_sample('leak.mod'))
    #  to be improved
    #  leak.mod has NEURON, PARAMETER, ASSIGNED, BREAKPOINT
    assert(len(parsed.asDict()) == 4)


def test_hh1():
    parsed = program.parseFile(get_sample('hh1.mod'))
    #  to be improved
    #  hh1.mod has TITLE, NEURON, UNITS, PARAMETER, ASSIGNED, BREAKPOINT,
    #  INITIAL, PROCEDURE(2), FUNCTION, STATE
    assert(len(parsed.asDict()) == 10)


def test_na():
    parsed = program.parseFile(get_sample('na.mod'))
    #  to be improved
    #  na.mod has NEURON, UNITS, PARAMETER, ASSIGNED, BREAKPOINT, INITIAL,
    #  PROCEDURE(2), DERIVATIVE, FUNCTION, STATE
    assert(len(parsed.asDict()) == 10)
