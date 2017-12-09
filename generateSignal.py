import scipy
from scipy import signal
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
import pickle

fs = 10e6 # Hz
pulseLen = 0.01 # sec
signalLen = 10 # sec

def writeSignal(mySignal):
    with open("sendSignal.pk", "wb") as outfile:
        pickle.dump(mySignal, outfile)

    with open("sendSignal.bin", "wb") as outfile:
        mySignal.tofile(outfile)

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

if __name__ == '__main__':
    data=[0,1,0,1,1,1,0,0,1]
    pulses = importPulses(2)

    pulseLen = len(pulses[0])
    numSamples = int(pulseLen * len(data))

    sigOut = np.zeros(numSamples, dtype=np.complex64)

    for i, x in enumerate(data):
        # print("{} : {}".format(i*pulseLen, (i+1)*pulseLen))
        sigOut[i*pulseLen:(i+1)*pulseLen] = pulses[x]

    writeSignal(sigOut)
