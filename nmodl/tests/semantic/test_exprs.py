from xml.dom import minidom
from nmodl.program import program
from nmodl.lems_generator import LemsCompTypeGenerator


def test_function():
    s = '''
    DERIVATIVE dx{
        x' = double(-x) + double(1)
    }
    FUNCTION double(arg){
        LOCAL d=2
        double = d * arg
    }'''
    LemsCompTypeGenerator().visit(program.parseString(s))


def test_procedure():
    pass


def test_time_derivative():
    pass
