from textwrap import dedent

import nmodl.expressions as ne


def test_stmt():
    assert(ne.expr.parseString('a = 10').asList() ==
           [['a', '=', '10']])


def test_if():
    assert(ne.ifstmt.parseString('if(1+1 ==2) 1\n else sin(0e-1)').asList() ==
           ['if', [['1', '+', '1'], '==', '2'], ['1'], 'else', ['sin', ['0e-1']]])


def test_body():
    stmts = dedent('''
            a = 1
            a + 1
            if(a == 12){
            1 + 1
            2 % 21}
            else
            sin(x)
            ''')
    assert(ne.body.parseString(stmts).asList() ==
           [[['a', '=', '1']],
            [['a', '+', '1']],
            ['if',
              ['a', '==', '12'],
              [[['1', '+', '1']], [['2', '%', '21']]],
              'else',
              ['sin', ['x']]]])


def test_func():
    fun = dedent('''
    funfun(ab, c(pF)){
        1+2.1
        if(c == 2){
        -42e-2
        }
    }
    ''')
    assert(ne.fundecl.parseString(fun).asList() ==
           [['funfun', [['ab'], ['c', 'pF']], 
             [[['1', '+', '2.1']],
              ['if', 
               ['c', '==', '2'],
               [[['-', '42e-2']]]]]]])

