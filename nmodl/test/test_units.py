from ..units import unit, units_blk

def test_unit():
    test_string = '(mV) = (millivolt)'
    assert(unit.parseString(test_string).asList() ==
           [['mV', '=', 'millivolt']])


def test_none():
    test_string = 'UNITS {}'
    assert(units_blk.parseString(test_string).asList() ==
           ['UNITS', []])

def test_two():
    from textwrap import dedent
    test_string = dedent("""
    UNITS {
        (mV) = (millivolt)
        (mA) = (milliamp)
    }
    """)
    assert(units_blk.parseString(test_string).asList() ==
           ['UNITS', ['mV', '=', 'millivolt'],['mA', '=', 'milliamp']])
