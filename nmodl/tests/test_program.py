from nmodl.program import program

print(program.parseString('''
TITLE test mod file

UNITS{
    (mV) = (millivolt)
}


COMMENT
  time flies
    \t like an arrow
  fruits flies
\t like a banana
ENDCOMMENT

ASSIGNED {
        v               (mV)
        celsius         (degC)
        ina             (mA/cm2)
        gna             (pS/um2)
        ena             (mV)
        minf            hinf
        mtau (ms)       htau (ms)
        tadj
}
UNITSOFF
PARAMETER{
    erev = -70  (mV) : comment till eol
    gnabar = .12 (mho/cm2) : one more
    COMMENT
        are inline comments allowed? I think so.
        : here as well?
    ENDCOMMENT
}
UNITSON
''').asDict())
