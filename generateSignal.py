import scipy
from scipy import signal
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
import pickle

fs = 10e6 # Hz
pulseLen = 0.1 # sec
signalLen = 10 # sec

numSamples = int(fs * signalLen)


with open("pacmansignal.pk", "rb") as infile:
    pacmanPulse = pickle.load(infile)

sigOut = np.random.random(numSamples) * 0.01

pulseLoc = np.random.randint(numSamples - len(pacmanPulse))
# print(pulseLoc)
sigOut[pulseLoc:pulseLoc+len(pacmanPulse)] += pacmanPulse


with open("signalIn.pk", "wb") as outfile:
    pickle.dump(sigOut, outfile)
