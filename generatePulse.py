import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


# Generate Pulse maps bits to pulse shapes
# 0: /
# 1: \
# 2: >
# 3: <
# bottom is low frequency, top is high
def generatePulse(bit, totalTime, sampleRate):
    if bit == 0:
        return generateFwdSlash(totalTime, sampleRate)
    if bit == 1:
        return generateBackSlash(totalTime, sampleRate)
    if bit == 2:
        return generateFwdAngleBracket(totalTime, sampleRate)
    if bit == 3:
        return generateBackAngleBracket(totalTime, sampleRate)


def generateFwdSlash(totalTime, sampleRate):
    # fs = samples/s
    # totalTime = # of seconds
    # # of samples = sampleRate * totalTime
    t = np.linspace(0, totalTime, totalTime * sampleRate)
    freqs = np.linspace(0, 2e6, totalTime * sampleRate - 1)  # hz

    # dphi/dt = 2*pi*f(t)
    # find phase differences than cumsum to get the total phase offset at each point
    dts = np.diff(t)
    dphis = 2*np.pi*freqs*dts
    phases = np.cumsum(dphis)
    phases = np.insert(phases, 0, 0)
    return np.cos(phases)


def generateBackSlash(totalTime, sampleRate):
    t = np.linspace(0, totalTime, totalTime * sampleRate)
    freqs = np.linspace(1e6, 0, totalTime * sampleRate)  # hz
    print freqs[-1] * t[-1]
    print np.multiply(freqs, t)[-1]
    return np.cos(2*np.pi*np.multiply(freqs, t))


def generateFwdAngleBracket(totalTime, sampleRate):
    pass


def generateBackAngleBracket(totalTime, sampleRate):
    pass

fs = 5e6
x = generatePulse(0, 0.1, fs)

f, t, Sxx = signal.spectrogram(x, fs)
plt.pcolormesh(t, f, Sxx)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()
