from xml.dom import minidom
from nmodl.program import program
from nmodl.lems_generator import LemsCompTypeGenerator


def test_function():
    s = '''
    DERIVATIVE dx{
        x' = mult(-x, 2) + mult(1, 2+1)
    }
    FUNCTION mult(arg1, arg2){
        LOCAL d
        d = arg2
        double = d * arg
    }'''
    LemsCompTypeGenerator().visit(program.parseString(s))


def test_procedure():
    pass


def test_time_derivative():
    pass
