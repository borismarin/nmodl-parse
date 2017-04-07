from tgt_model import _ik
from numpy import zeros
from pylab import plot


n = zeros(10000)
ik = _ik()
ext = {'v': -60., 'ek': -70, 'n': 0}
n[0] = ik.initial(ext)['n']
ext['n'] = n[0]

dt = 0.01
for i in range(9999):
    ext['v'] = 0 if i > 3999 and i < 6000 else -60.
    ext['n'] = n[i + 1] = n[i] + dt * ik.derivative(ext)['n']

plot(dt * arange(10000), n, 'o')
