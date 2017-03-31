from nmodl.unparse import unparse


def test_title():
    from nmodl.title import title
    title_only = 'TITLE nana'
    p = title.parseString(title_only)[0]
    assert(unparse(p) == title_only)

    p.title = 'another'
    assert(unparse(p) == 'TITLE another')


def test_units():
    from nmodl.units import units_blk
    from textwrap import dedent
    un = dedent("""
    UNITS {
        (mV) = (millivolt)
        (mA) = (milliamp)
    }""")
    p = units_blk.parseString(un)[0]
    assert(unparse(p) == un)

