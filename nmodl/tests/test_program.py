from nmodl.program import program

print(program.parseString('''
TITLE test mod file
UNITS{
    (mV) = (millivolt)
}
PARAMETER{
    erev = -70  (mV)
    gnabar = .12 (mho/cm2)
}
''').asDict())
