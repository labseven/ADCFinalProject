import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import misc
from scipy import signal
import pickle

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

for convolve in convolves:
    plt.plot(abs(convolve))
plt.show()
