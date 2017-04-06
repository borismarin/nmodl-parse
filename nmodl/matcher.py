from __future__ import division
import sympy as sp


def match_hhexp(expr_str):
    expr = sp.nsimplify(expr_str)
    rate, arg0 = sp.symbols('rate arg0', cls=sp.Wild)
    v, mid, scale = sp.symbols('v mid scale')
    rough = rate * sp.exp(arg0)
    rough_m = expr.match(rough)
    rate = rough_m[rate]
    arg1 = rough_m[arg0]
    inner = -(v - mid)/scale
    inner_m = sp.solve(arg1 - inner, [mid, scale])
    if(rough_m and inner_m):
        return {'rate': rate,
                'midpoint': inner_m[mid],
                'scale': inner_m[scale]}


def test_hh_alpha_n():
    assert(match_hhexp('0.125 * exp(-(v + 65) / 80)') ==
           {'rate': 0.125, 'midpoint': -65, 'scale': 80})
