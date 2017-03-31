from nmodl.title import title


def test_single():
    test_string = "TITLE time"
    assert(title.parseString(test_string)[0].parsed.asList() == 
           ['TITLE', 'time'])


def test_multi():
    test_string = "TITLE time flies like an arrow"
    assert(title.parseString(test_string)[0].parsed.asList() == 
           ['TITLE', 'time flies like an arrow'])


def test_obj():
    test_string = "TITLE time flies like an arrow"
    assert(title.parseString(test_string)[0].title == 
           'time flies like an arrow')

