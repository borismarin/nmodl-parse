from nmodl.state import state_blk


def test_state():

    assert(state_blk.parseString("STATE{abc}").asList() ==
           ['STATE', 'abc'])

    test_string = 'STATE {x y \n\n\t wz\n}'
    assert(state_blk.parseString(test_string).asList() ==
           ['STATE', 'x', 'y', 'wz'])


def test_state_units():
    sv = state_blk.parseString("STATE{a (mV) b c (mM)}").state_vars
    assert(sv[0].id == 'a')
    assert(sv[0].unit == 'mV')
    assert(sv[1].id == 'b')
    assert(sv[2].asList() == ['c', 'mM'])
