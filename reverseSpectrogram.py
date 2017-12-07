import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from scipy import signal
import pickle


# Need to figure out how many samples 'tall' the image should be
fs = 10e6
t = np.linspace(0,.1,fs*.1)
s = np.cos(2*np.pi*t*2e6)

fftCos = np.fft.fft(s)
print(fftCos.shape)
plt.plot(fftCos)
plt.show()


f = misc.imread('pacman.png', flatten=True)

# Turn it into the fft of what we want (negative freq)
im = np.zeros((f.shape[0]*2, f.shape[1]))
im[:][:f.shape[0]] = f
im[:][f.shape[0]:] = f[::-1]

plt.imshow(im.T)
plt.show()

x = np.zeros(im.shape[0]*im.shape[1])

for i, column in enumerate(im.T):
    signalWindow = np.fft.ifft(column)
    x[i*im.shape[0]:(i+1)*im.shape[0]] = signalWindow

x = x/max(abs(x))
with open("pacmansignal.pk", "wb") as outfile:
    pickle.dump(x, outfile)

plt.plot(x.real)
plt.plot(x.imag)
plt.show()

f, t, Sxx = signal.spectrogram(x, fs=fs, nperseg=f.shape[1])
plt.pcolormesh(t, f/1e6, Sxx)
plt.ylabel('Frequency [MHz]')
plt.xlabel('Time [sec]')
plt.show()
