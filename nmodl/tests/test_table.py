from textwrap import dedent

from nmodl.table import table


def test_table():
    s = dedent('''
    TABLE minf,  hinf
    DEPEND celsius, temp
    FROM vmin TO vmax WITH 199
    ''')
    assert(table.parseString(s).asList() ==
           ['TABLE', 'minf', 'hinf',
            'DEPEND', 'celsius', 'temp',
            'FROM', 'vmin', 'TO', 'vmax', 'WITH', '199']
           )
