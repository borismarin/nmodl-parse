from nmodl.state import state_blk


def test_state():

    assert(state_blk.parseString("STATE{abc}").asList() ==
           ['STATE', ['abc']]) 

    from textwrap import dedent
    test_string = dedent("""
    STATE {x y 
    
    wz}
    """)
    assert(state_blk.parseString(test_string).asList() ==
           ['STATE', ['x', 'y', 'wz']])
