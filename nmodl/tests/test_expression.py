import nmodl.expressions as ne


def test_stmt():
    assert(ne.stmt.parseString('a = 10').asList() == [['a', '=', '10']])


def test_if():
    assert(ne.if_stmt.parseString('if(1+1==2)x=1\n else x=sin(0e-1)')
           .asList() ==
           ['if',
            [['1', '+', '1'], '==', '2'],
            ['x', '=', '1'],
            'else', ['x', '=', 'sin', ['0e-1']]])


def test_if2():
    assert(ne.if_stmt.parseString('if(abs(-1)==1)tan(pi/4)\n else log(-1)')
           .asList() ==
           ['if',
            ['abs', [['-', '1']], '==', '1'],
            'tan',
            [['pi', '/', '4']],
            'else',
            'log',
            [['-', '1']]])


def test_logical():
    assert(ne.expr.parseString('x>1 && x<1.0e0')
           .asList() ==
           [[['x', '>', '1'], '&&', ['x', '<', '1.0e0']]])


def test_nested_func():
    assert(ne.stmt.parseString('sin(arcsin(1))').asList() ==
           ['sin', ['arcsin', ['1']]])


def test_funcdef():
    from textwrap import dedent
    f = dedent('''
    funfun(x(mV), g(mS)){
         funfun = x * g
    }
    ''')
    assert(ne.func_def.parseString(f).asList() ==
           ['funfun', [['x', 'mV'], ['g', 'mS']],
            [['funfun', '=', ['x', '*', 'g']]]])

def test_funcdef_units():
    from textwrap import dedent
    f = dedent('''
    funfun(x(mV), g(mS))(/ms){
         funfun = x * g
    }
    ''')
    assert(ne.func_def.parseString(f).asList() ==
           ['funfun', [['x', 'mV'], ['g', 'mS']], '/ms',
            [['funfun', '=', ['x', '*', 'g']]]])


def test_pow():
    assert(ne.expr.parseString('e^(2 * pi)').asList() ==
           [['e', '^', ['2', '*', 'pi']]])


def test_unit():
    assert(ne.expr.parseString(
        'tadj = q10^((celsius - temp)/(10 (degC)))').asList() ==
        [['tadj', '=', 
          ['q10', '^', [['celsius', '-', 'temp'], '/', '10', 'degC']]]])
