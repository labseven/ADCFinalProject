import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import misc
from scipy import signal
import pickle
from pylab import *
import obspy
import obspy.signal
import obspy.signal.filter

def importPulses(numPulses):
    pulses = []
    for i in range(numPulses):
        filename ='pulses/{}.pk'.format(i)
        print("importing {}".format(filename))

        with open(filename, "rb") as infile:
            pulse = pickle.load(infile)
            pulses.append(pulse)

    pulseLen = len(pulses[0])
    for pulse in pulses:
        assert len(pulse) == pulseLen

    return pulses

def importSignal():
    print("importing signal")
    sigIn = scipy.fromfile(open("usrpSink.bin"), dtype=scipy.complex64)
    return sigIn

def saveConvolve(filename, convolve):
    print("saving pulse {}: {} samples".format(filename, len(convolve)))
    with open("pulses/out{}.pk".format(filename), "wb") as outfile:
        pickle.dump(convolve, outfile)

# f, t, Sxx = signal.spectrogram(sigIn.real)
# plt.pcolormesh(t, f/1e6, Sxx)
# plt.ylabel('Frequency [MHz]')
# plt.xlabel('Time [sec]')
# plt.show()

pulses = importPulses(2)
recSignal = importSignal()

convolves = []
for i, pulse in enumerate(pulses):
    print("convolve {}".format(i))
    convolve = signal.fftconvolve(abs(recSignal), pulse)
    convolves.append(convolve)
    # saveConvolve(i, convolve)
#for convolve in convolves:
#    plt.plot(abs(convolve))
#
#plt.show()

ds_convolves = []
for convolve in convolves:
    ds_convolve = convolve[::1000]
    ds_convolves.append(ds_convolve)

for ds_convolve in ds_convolves:
    plt.plot(abs(ds_convolve))

legend(['pacman', 'ghost'])
plt.show()

for ds_convolve in ds_convolves:
    #m_hat = abs(scipy.signal.hilbert(abs(ds_convolve),N=100))
    #print 'm_hat'
    data_envelope = obspy.signal.filter.envelope(abs(ds_convolve))
    plot(abs(ds_convolve))
    #plot(m_hat)
    plot(data_envelope)
    axis('tight')
    legend(['x', 'data_envelope'])
    show()

starts = []
ends = []
for ds_convolve in ds_convolves:
    abs_ds_convolve = abs(ds_convolve)
    my_envelope = []
    my_env_int = []
    pos = 0
    for i in abs_ds_convolve:
        #print i
        if i > .3:
            my_envelope.append(i)
            #print my_envelope
            my_env_int.append(pos)
            #print my_env_int
        pos = pos+1
    start = [0]
    end = []
    last_i = 0
    for i in my_env_int:
        diff = i - last_i
        if diff > 200:

            end.append(last_i)
            start.append(i)
        last_i = i
    #print start
    #print end
    plot(abs(ds_convolve))
    plot(my_env_int, my_envelope)
    show()

    starts.append(start)
    ends.append(end)

ghost = False
print starts[0]
print 'starts[0]'
for i in starts[0]:
    #print 'i' + str(i)
    array = np.linspace(i,i+600,601)
    #print array
    for a in array:
        ghost = False
        thing = ds_convolves[1]
        #print thing[int(a)]
        if abs(thing[int(a)]) > .5:
            print str('ghost ') + str(a)
            ghost = True
            break
        continue
    if ghost == False:
        print 'pacman' + str(i)
        
    

#print starts
#print ends


