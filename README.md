# nmodl-parse
[![Build Status](https://travis-ci.org/borismarin/nmodl-parse.svg?branch=master)](https://travis-ci.org/borismarin/nmodl-parse)

Primitive, incomplete parser for _NEURON_ `.mod` files using _pyparsing_.

Initial goals:
 - swallow an acceptable number of 'real' `.mod` files, even if we are not trying to be comprehensive
 - build an internal representation complete enough to be used for src2src compiling `.mod` to _NeuroML2/LEMS_ (nothing very smart, heuristics to be added later).

See also:

https://www.neuron.yale.edu/neuron/static/docs/help/neuron/nmodl/nmodl.html

http://cns.iaf.cnrs-gif.fr/files/scopman.html

https://www.neuron.yale.edu/neuron/static/papers/nc2000/nmodl400.pdf
