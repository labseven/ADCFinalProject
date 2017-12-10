import scipy
from scipy import signal
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
import pickle
import sys
from huffmanEncoding import *

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
    message = sys.argv[1]

    _, huffDict = genHuffmanFromFile('english.txt')
    data = encodeHuffman(huffDict, message)

    pulses = importPulses(2)

    fs = 320e3
    print("fs: {}".format(fs))

    pulseLen = len(pulses[0])
    numSamples = int(pulseLen * len(data))

    sigOut = np.zeros(numSamples, dtype=np.complex64)

    for i, x in enumerate(data):
        # print("{} : {}".format(i*pulseLen, (i+1)*pulseLen))
        sigOut[i*pulseLen:(i+1)*pulseLen] = pulses[x]

    print("sigOut: {} samples {} seconds".format(len(sigOut), len(sigOut)/fs))
    writeSignal(sigOut)
