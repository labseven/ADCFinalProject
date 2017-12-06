import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from scipy import signal

f = misc.imread('pacman.png', flatten=True)

# Turn it into the fft of what we want (negative freq)
im = np.zeros((f.shape[0]*2, f.shape[1]))
im[:][:f.shape[0]] = f
im[:][f.shape[0]:] = f[::-1]

plt.imshow(im)
plt.show()

x = np.zeros(im.shape[0]*im.shape[1])

for i, column in enumerate(im.T):
    signalWindow = np.fft.ifft(column)
    x[i*im.shape[0]:(i+1)*im.shape[0]] = signalWindow


plt.plot(x.real)
plt.plot(x.imag)
plt.show()

f, t, Sxx = signal.spectrogram(x, fs=10, nperseg=f.shape[1])
plt.pcolormesh(t, f/1e6, Sxx)
plt.ylabel('Frequency [MHz]')
plt.xlabel('Time [sec]')
plt.show()
