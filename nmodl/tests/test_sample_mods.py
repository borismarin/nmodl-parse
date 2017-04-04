import os
from nmodl.program import program


def get_sample(fname):
    return os.path.join(os.path.dirname(__file__), 'sample_mods', fname)


def all_in(parsed, list):
    return all(k in parsed.keys() for k in list)


def test_passive():
    p = program.parseFile(get_sample('passiv.mod'))
    assert(all_in(p, ('neuron', 'parameter', 'assigned', 'breakpoint')))


def test_leak():
    p = program.parseFile(get_sample('leak.mod'))
    assert(all_in(p, ('neuron', 'parameter', 'assigned', 'breakpoint')))


def test_hh1():
    p = program.parseFile(get_sample('hh1.mod'))
    assert(all_in(p, ('title', 'neuron', 'units', 'parameter', 'assigned',
                      'breakpoint', 'initial', 'procedures', 'functions',
                      'state')))


def test_na():
    p = program.parseFile(get_sample('na.mod'))
    assert(all_in(p, ('neuron', 'units', 'parameter', 'assigned', 'breakpoint',
                      'initial', 'procedures', 'functions', 'state')))
