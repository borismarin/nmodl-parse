from textwrap import dedent
from nmodl.procedure import procedure_blk


def test_procedure():
    assert(procedure_blk.parseString('PROCEDURE a(){x=1}').asList() ==
           ['PROCEDURE', 'a', [['x', '=', '1']]])


def test_procedure_locals_tables():
    fun = dedent('''
    PROCEDURE rates(vm (mV)){
    LOCAL a,b
    TABLE h DEPEND celsius FROM 0 TO 1 WITH 200
    a = Ra
    b = Rg
    h = 1/(a+b)}
    ''')
    assert(procedure_blk.parseString(fun).asList() ==
           ['PROCEDURE',
            'rates',
            [['vm', 'mV']],
            ['LOCAL', 'a', 'b',
             'TABLE', 'h', 'DEPEND', 'celsius', 'FROM', '0', 'TO', '1', 'WITH', '200',
             ['a', '=', 'Ra'],
             ['b', '=', 'Rg'],
             ['h', '=', ['1', '/', ['a', '+', 'b']]]]])
