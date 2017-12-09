import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import misc
from scipy import signal
import pickle

with open("pacmansignal.pk", "rb") as infile:
    pacmanPulse = pickle.load(infile)

sigIn = scipy.fromfile(open("inFile"), dtype=scipy.complex64)

# with open("signalIn.pk", "rb") as infile:
#     sigIn = pickle.load(infile)


# f, t, Sxx = signal.spectrogram(sigIn.real)
# plt.pcolormesh(t, f/1e6, Sxx)
# plt.ylabel('Frequency [MHz]')
# plt.xlabel('Time [sec]')
# plt.show()


print(pacmanPulse.shape)
print(sigIn.shape)

# plt.plot(sigIn[::1000])
# plt.show()

x = signal.fftconvolve(sigIn, pacmanPulse)

print(len(x))
plt.plot(x[::int(len(x)/100000)])
plt.show()
