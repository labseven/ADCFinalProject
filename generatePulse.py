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
    w = 3e6  # hz
    return np.cos(2*np.pi*w*np.linspace(0, totalTime, totalTime * sampleRate))


def generateBackSlash(totalTime, sampleRate):
    pass


def generateFwdAngleBracket(totalTime, sampleRate):
    pass


def generateBackAngleBracket(totalTime, sampleRate):
    pass

fs = 10e6
x = generatePulse(0, 0.1, fs)

f, t, Sxx = signal.spectrogram(x, fs)
plt.pcolormesh(t, f, Sxx)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()
