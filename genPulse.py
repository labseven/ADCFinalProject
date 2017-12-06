import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


# Generate Pulse maps bits to pulse shapes
# 0: /
# 1: \
# 2: >
# 3: <
# bottom is low frequency, top is high
def genPulse(bit, totalTime, sampleRate):
    if bit == 0:
        return genFwdSlash(totalTime, sampleRate)
    if bit == 1:
        return genBackSlash(totalTime, sampleRate)
    if bit == 2:
        return genFwdAngleBracket(totalTime, sampleRate)
    if bit == 3:
        return genBackAngleBracket(totalTime, sampleRate)


def genFwdSlash(totalTime, sampleRate):
    # fs = samples/s
    # totalTime = # of seconds
    # # of samples = sampleRate * totalTime
    t = np.linspace(0, totalTime, totalTime * sampleRate)
    freqs = np.linspace(0, 2e6, totalTime * sampleRate)  # hz
    return genSig(t, freqs)


def genBackSlash(totalTime, sampleRate):
    t = np.linspace(0, totalTime, totalTime * sampleRate)
    freqs = np.linspace(2e6, 0, totalTime * sampleRate)  # hz
    return genSig(t, freqs)


def genFwdAngleBracket(totalTime, sampleRate):
    pass


def genBackAngleBracket(totalTime, sampleRate):
    pass


# Generates a signal of varying frequencies
# ts are the time domains
# freqs are the frequencies at corresponding times
# len(ts) must equal len(freqs) = len(return value)
def genSig(ts, freqs):
    # dphi/dt = 2*pi*f(t)
    # find phase differences than cumsum to get the total phase offset at each point
    dts = np.diff(ts)
    dphis = 2*np.pi*freqs[:-1]*dts
    phases = np.cumsum(dphis)
    phases = np.insert(phases, 0, 0)
    return np.cos(phases)



fs = 5e6
x = genPulse(1, 0.1, fs)

f, t, Sxx = signal.spectrogram(x, fs)
plt.pcolormesh(t, f, Sxx)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()
