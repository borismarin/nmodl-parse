from textwrap import dedent
from nmodl.function import function_blk


def test_func():
    fun = dedent('''
    FUNCTION efun(z) {
        if (fabs(z) < 1e-6) {
            efun = 1 - z/2
        }else{
            efun = z/(exp(z) - 1)
        }
    }''')
    assert(function_blk.parseString(fun).asList() ==
           ['FUNCTION',
            'efun',
            [['z']],
            ['if',
             ['fabs', ['z'], '<', '1e-6'],
             ['efun', '=', ['1', '-', ['z', '/', '2']]],
             'else',
             ['efun', '=', ['z', '/', ['exp', ['z'], '-', '1']]]]])
