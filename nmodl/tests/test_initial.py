from textwrap import dedent
from nmodl.initial import initial_blk
from nmodl.comment import comments

def test_initial():
    fun = dedent('''
    INITIAL {
        tadj = q10^((celsius - temp)/(10 (degC))) : make all threads calculate tadj at initialization

        trates(v+vshift)
        m = minf
        h = hinf
    }
    ''')
    assert(initial_blk.ignore(comments).parseString(fun).asList() ==
           ['INITIAL',
            ['tadj', '=', ['q10', '^', [['celsius', '-', 'temp'], '/', '10', 'degC']]],
            'trates',
            [['v', '+', 'vshift']],
            ['m', '=', 'minf'],
            ['h', '=', 'hinf']])
