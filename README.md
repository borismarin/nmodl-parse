# nmodl-parse
[![Build Status](https://travis-ci.org/borismarin/nmodl-parse.svg?branch=master)](https://travis-ci.org/borismarin/nmodl-parse)

Tentative parser for _NEURON_ `.mod` files using _pyparsing_.

If you are interested in doing anything complex (e.g. transpiling) with the parsed file, consider using the [pynmodl](https://github.com/borismarin/pynmodl) project, which provides better infrastructure and sample compilers (at the moment, `mod`->`LEMS`, unparser).

The code in master already parses a number of [garden-variety `mod`files](nmodl/tests/sample_mods/). Given our more ambitious goal of compiling `mod` to [`LEMS`](https://github.com/LEMS/LEMS), and that parsing is just a small part of compilation, we have decided to adopt a 'language-workbench' approach with [textX](https://github.com/igordejanovic/textx) which can be found at https://github.com/borismarin/pynmodl.

See also:

https://www.neuron.yale.edu/neuron/static/docs/help/neuron/nmodl/nmodl.html

http://cns.iaf.cnrs-gif.fr/files/scopman.html

https://www.neuron.yale.edu/neuron/static/papers/nc2000/nmodl400.pdf
