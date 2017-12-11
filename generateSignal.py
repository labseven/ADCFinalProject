import scipy
from scipy import signal
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
import pickle
import sys
from huffmanEncoding import *

"""
Signal generation library.
Author: Adam Novotny

main:
    Arguments:
        1: "message"
    generates huffman code tree
    encodes message (argv[1]) in huffman codes
    packetizes data
    creates signal using pulses
    saves signal to sendSignal.bin

writeSignal(outSignal)
    writes a signal to sendSignal.pk and sendSignal.bin
    Returns: nothing

importPulses(numPulses)
    imports pulses from pulses/{0-numPulses}.pk
    Returns: list of pulse data

packetizeData(data, header=[1,0])
    packetizes a datastream
    [1,0] + header + [error code bit]
    sum(packet)%2 = 0
    Returns: list of packets [[1,0,1 ... 0], [1,0,0 ... 1]]
"""

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

def packetizeData(data, header=[1,0]):
    # Make data divisible by 8
    data = data + [0]*(8-len(data)%8)

    stream = []
    for i in xrange(len(data)/8):
        packetData = header + data[i*8:(i+1)*8]
        # Add error correction bit
        packetData.append((sum(packetData)%2))
        # print(packetData)
        stream.append(packetData)

    return stream

if __name__ == '__main__':
    message = sys.argv[1]

    _, huffDict = genHuffmanFromFile('english.txt')
    data = encodeHuffman(huffDict, message)

    bitstream = packetizeData(data)
    print(bitstream)

    pulses = importPulses(2)

    fs = 320e3
    print("fs: {}".format(fs))

    pulseLen = len(pulses[0])
    numSamples = int(pulseLen * (len(bitstream[0]) + 1))

    signals = np.zeros((len(bitstream), numSamples), dtype=np.complex64)
    for i, packet in enumerate(bitstream):
        for j, bit in enumerate(packet):
            signals[i][j*pulseLen:(j+1)*pulseLen] = pulses[bit]

    sigOut = signals.flatten()

    # plt.plot(sigOut[::100])
    # plt.show()

    print("sigOut: {} samples {} seconds".format(len(sigOut), len(sigOut)/fs))
    writeSignal(sigOut)
