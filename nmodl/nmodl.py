from units import units_blk
from title import title

script = title + units_blk

print(script.parseString('''
TITLE test mod file
UNITS{
(mV) = (millivolt)
}
'''))
