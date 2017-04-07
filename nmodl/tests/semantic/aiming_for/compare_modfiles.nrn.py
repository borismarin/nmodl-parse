#!/usr/bin/ipython -i

from neuron import h


def create_comp(name='soma'):
    comp = h.Section(name)

    comp.nseg = 1
    comp.L = 100
    comp.diam = 500

    comp.insert('kd_original')
    comp.gkbar_kd_original = 0.0
    comp.ek = -60

    comp.insert('kd')
    comp.gmax_kd = 0.0
    comp.ek = -60

    comp.insert('pas')
    comp.g_pas = 0.001
    comp.e_pas = -60

    return comp


def get_next_hex_color():
    from random import randint
    return "#%06x" % randint(0, 0xFFFFFF)


def plot_timeseries(vdict, varlist):
    import matplotlib.pyplot as plt
    t = vdict['t']
    v = vdict['v']
    fig = plt.figure(figsize=(5, 6))

    ax = fig.add_subplot(2, 1, 1)
    ax.plot(t, v, 'k-', linewidth=2)
    ax.set_title('membrane potential')
    ax.set_xlim([0, 500])

    ax2 = fig.add_subplot(2, 1, 2)
    for n in range(1, len(varlist)):
        ax2.plot(t, vdict[varlist[n]], label=varlist[n],
                 color=get_next_hex_color(), linewidth=2)
    ax2.set_title('recorded gating variables')
    ax2.set_xlim([0, 500])
    ax2.set_xlabel('Time [ms]')
    ax2.set_ylim([0, 1])

    from numpy import loadtxt
    l = loadtxt('jlems_ik_test.dat')
    ax2.plot(l[:, 0]*1000, l[:, 2], '-k', label='nml')

    l = loadtxt('jlems_ik_lems_test.dat')
    ax2.plot(l[:, 0]*1000, l[:, 2], '-r', label='lems')

    ax2.legend()
    plt.show()


def create_dumps(section, varlist):
    recordings = {n: h.Vector() for n in varlist}

    for (vn, v) in recordings.iteritems():
        v.record(section(0.5).__getattribute__('_ref_' + vn))

    recordings['t'] = h.Vector()
    recordings['t'].record(h._ref_t)
    return recordings


def dump_to_file(vdict, varlist, fname='neuron_ik_test.dat'):
    from numpy import savetxt, array

    vnames = ['t'] + varlist
    X = array([vdict[x].to_python() for x in vnames]).T
    savetxt(fname, X)


def run(tstop=10, dt=0.001):
    h.dt = dt
    h.finitialize(-70.0)
    h.fcurrent()
    h.frecord_init()
    while h.t < tstop:
        h.fadvance()


comp = create_comp('soma')
h.celsius = 24

inputs = []

stim = h.IClamp(0.5, sec=comp)
stim.delay = 100
stim.dur = 100
stim.amp = -2
inputs.append(stim)

stim = h.IClamp(0.5, sec=comp)
stim.delay = 200
stim.dur = 200
stim.amp = 2
inputs.append(stim)


varlist = ['v', 'n_kd_original', 'n_q_kd']
ds = create_dumps(comp, varlist)

run(500, 0.001)

plot_timeseries(ds, varlist)
dump_to_file(ds, varlist)
