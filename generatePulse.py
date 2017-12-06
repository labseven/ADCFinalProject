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
    numSamples = int(totalTime * sampleRate)
    # fs = samples/s
    # totalTime = # of seconds
    # # of samples = sampleRate * totalTime
    t = np.linspace(0, totalTime, numSamples)


    """ Interestingly, when using just linspace, then it reaches 4MHz.
    When doing discrete climbing, it goes only up to 2MHz"""
    # freqs = np.linspace(0, 2e6, numSamples*10000)

    freqs = np.full(numSamples // 10000, 2e6)
    freqs[:(numSamples// 10000) //2] = np.linspace(0, 2e6, (numSamples// 10000) //2)  # hz
    freqs = np.repeat(freqs, 10000)


    plt.plot(t,freqs)
    plt.plot(t, t*freqs)
    plt.show()

    return np.cos(2*np.pi*t*freqs)


def generateBackSlash(totalTime, sampleRate):
    pass


def generateFwdAngleBracket(totalTime, sampleRate):
    pass


def generateBackAngleBracket(totalTime, sampleRate):
    pass

fs = 10e6
x = generatePulse(0, .1, fs)

f, t, Sxx = signal.spectrogram(x, fs, nperseg=1024)
plt.pcolormesh(t, f/1e6, Sxx)
plt.ylabel('Frequency [MHz]')
plt.xlabel('Time [sec]')
plt.show()
