import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from scipy import signal
from scipy import ndimage
from skimage.transform import resize
import pickle
from numpy.fft import fftfreq, ifft, fftshift


# Need to figure out how many samples 'tall' the image should be
fs = 4e6
# t = np.linspace(0,.1,fs*.1)
# s = np.cos(2*np.pi*t*2e6)

# fftCos = fft(s)
# print(fftCos.shape)
# plt.plot(fftfreq(fftCos.shape[0]))
# plt.plot(fftCos)
# plt.show()


f = misc.imread('dot.png', flatten=True, mode='F')
print(np.max(f))
# pacman /= 255
# f = pacman[::2][:] # resize(pacman, (pacman.shape[0]/4, pacman.shape[1]/4))
# f = ndimage.gaussian_filter(pacman, sigma=100)

# Turn it into the fft of what we want (negative freq)
im = np.zeros((f.shape[0]*2, f.shape[1]))
im[:][:f.shape[0]] = f
im[:][f.shape[0]:] = f[::-1]

# plt.imshow(im.T)
# plt.show()
print(im.shape)
print(len(im.T[0]))
print(np.max(fftfreq(len(im.T[0]))))

x = np.zeros(im.shape[0]*im.shape[1], dtype=np.complex64)

# slice up image and take ifft of each slice
for i, column in enumerate(im.T[::21]):
    signalWindow = fftshift(ifft(column))
    # plt.subplot(2, 1, 1)
    # plt.plot(column)
    # plt.subplot(2, 1, 2)
    # plt.plot(fftshift(signalWindow))
    # plt.show()
    x[i*im.shape[0]:(i+1)*im.shape[0]] = signalWindow

x = x/max(abs(x))

with open("pacmansignal.pk", "wb") as outfile:
    pickle.dump(x, outfile)

with open("pacmansignal.bin", "wb") as outfile:
    x.tofile(outfile)

print("save successful")

plt.plot(x.real)
plt.plot(x.imag)
plt.title("Signal")
plt.xaxis("time")
plt.yaxis("magnitude")
plt.show()

f, t, Sxx = signal.spectrogram(x, fs=fs, nperseg=f.shape[1]*2)
print(t)
# Divide by 1e6 because we are showing Mhz
plt.pcolormesh(t, f/1e6, Sxx)
plt.axis([0, 0.1, 0, 2])
plt.ylabel('Frequency [MHz]')
plt.xlabel('Time [sec]')
plt.show()
