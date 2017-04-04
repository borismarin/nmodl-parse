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
    assert(all(k in parsed.keys() for k in ('title', 'neuron', 'units',
                                            'parameter', 'assigned',
                                            'breakpoint', 'initial',
                                            'procedures', 'functions', 'state')))


def test_na():
    parsed = program.parseFile(get_sample('na.mod'))
    #  to be improved
    assert(all(k in parsed.keys() for k in ('neuron', 'units', 'parameter',
                                            'assigned', 'breakpoint',
                                            'initial', 'procedures', 'functions',
                                            'state')))
