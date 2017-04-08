# nmodl-parse
[![Build Status](https://travis-ci.org/borismarin/nmodl-parse.svg?branch=master)](https://travis-ci.org/borismarin/nmodl-parse)

Primitive, incomplete parser for _NEURON_ `.mod` files using _pyparsing_.

Initial goals:
 - swallow an acceptable number of 'real' `.mod` files (see [tests](nmodl/tests/test_sample_mods.py))
 - build a q&d LEMS/NeuroML generator. We are currently aiming for mechs
   directly usable inside a NeuroML cell, so some ad-hoc elements will be inserted.

See also:

https://www.neuron.yale.edu/neuron/static/docs/help/neuron/nmodl/nmodl.html

http://cns.iaf.cnrs-gif.fr/files/scopman.html

https://www.neuron.yale.edu/neuron/static/papers/nc2000/nmodl400.pdf
