from nmodl.unparse import unparse


def test_title():
    from nmodl.program import title
    title_only = 'TITLE nana'
    p = title.title.parseString(title_only)[0]
    assert(unparse(p) == title_only)

    p.title = 'another'
    assert(unparse(p) == 'TITLE another')
