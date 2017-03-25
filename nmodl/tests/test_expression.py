import nmodl.expressions as ne


def test_stmt():
    assert(ne.Statement.parseString('a = 10').asList() == ['a', '10'])


def test_if():
    assert(ne.Statement.parseString('if(1+1==2)x=1\n else x=sin(0e-1)')
           .asList() ==
           ['if', '1', '+', '1', '==', '2',
            'x', '1',
            'else', 'x', 'sin', '0e-1'])


def test_if2():
    assert(ne.IfStatement.parseString('if(abs(-1)==1)tan(pi/4)\n else log(-1)')
           .asList() ==
           ['if',
            'abs', '-1', '==', '1', 'tan', 'pi', '/', '4',
            'else', 'log', '-1'])


def test_logical():
    assert(ne.LogExp.parseString('x>1 && x<1.0e0')
           .asList() ==
           ['x', '>', '1', '&&', 'x', '<', '1.0e0'])


