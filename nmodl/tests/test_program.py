import pprint
from nmodl.program import program

p = program.parseString('''
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

PROCEDURE useless(){
    LOCAL a
    a = 42
}
FUNCTION efun(z) {
        if (fabs(z) < 1e-6) {
                efun = 1 - z/2
        }else{
                efun = z/(exp(z) - 1)
        }
}

NEURON {
    THREADSAFE
        SUFFIX na
        USEION na READ ena WRITE ina
        RANGE m, h, gna, gbar
        GLOBAL tha, thi1, thi2, qa, qi, qinf, thinf
        RANGE minf, hinf, mtau, htau
        GLOBAL Ra, Rb, Rd, Rg
        GLOBAL q10, temp, tadj, vmin, vmax, vshift
        }

STATE { m h }

BREAKPOINT {
        SOLVE states METHOD cnexp
        gna = tadj*gbar*m*m*m*h
        ina = (1e-4) * gna * (v - ena)
}


PROCEDURE trates(v (mV)) {
        TABLE minf,  hinf, mtau, htau
        DEPEND celsius, temp, Ra, Rb, Rd, Rg, tha, thi1, thi2, qa, qi, qinf
        FROM vmin TO vmax WITH 199

        rates(v): not consistently executed from here if usetable == 1

        tinc = -dt * tadj

        mexp = 1 - exp(tinc/mtau)
        hexp = 1 - exp(tinc/htau)
}


INITIAL {
    tadj = q10^((celsius - temp)/(10 (degC))) : make all threads calculate tadj at initialization

        trates(v+vshift)
        m = minf
        h = hinf
}

DERIVATIVE states {   :Computes state variables m, h, and n
        trates(v+vshift)      :             at the current v and dt.
        m' =  (minf-m)/mtau
        h' =  (hinf-h)/htau
}



''', parseAll=True)

pprint.PrettyPrinter().pprint(p.asDict())



