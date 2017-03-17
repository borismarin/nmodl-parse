NEURON {
SUFFIX leak
NONSPECIFIC_CURRENT i
RANGE i, e, g
}
PARAMETER {
g = 0.001 (siemens/cm2) < 0, 1e9 >
e = -65 (millivolt)
}
ASSIGNED {
i (milliamp/cm2)
v (millivolt)
}
BREAKPOINT { i = g*(v - e) }