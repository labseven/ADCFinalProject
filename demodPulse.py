import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from scipy import signal
import pickle

with open("pacmansignal.pk", "rb") as infile:
    pacmanPulse = pickle.load(infile)

with open("signalIn.pk", "rb") as infile:
    sigIn = pickle.load(infile)

print(pacmanPulse.shape)
print(sigIn.shape)

plt.plot(sigIn[::1000])
plt.show()

x = signal.fftconvolve(sigIn, pacmanPulse)

plt.plot(x[::1000])
plt.show()
