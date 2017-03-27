from textwrap import dedent
from nmodl.initial import initial_blk


def test_initial():
    fun = dedent('''
    INITIAL {

        trates(v+vshift)
        m = minf
        h = hinf
    }
    ''')
    assert(initial_blk.parseString(fun).asList() ==
           ['INITIAL',
            'trates',
            [['v', '+', 'vshift']],
            ['m', '=', 'minf'],
            ['h', '=', 'hinf']])
