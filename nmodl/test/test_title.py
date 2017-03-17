from nmodl.title import title


def test_single():
    test_string = "TITLE time"
    assert(title.parseString(test_string).asList() == 
           ['TITLE', 'time'])


def test_multi():
    test_string = "TITLE time flies like an arrow"
    assert(title.parseString(test_string).asList() == 
           ['TITLE', 'time flies like an arrow'])


def test_with_others():
    from textwrap import dedent
    test_string = dedent("""
    TITLE time flies like an arrow
    UNITS {}
    """)
    assert(title.parseString(test_string).asList() ==
           ['TITLE', 'time flies like an arrow'])

