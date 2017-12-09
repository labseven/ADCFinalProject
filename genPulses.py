import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from scipy import signal
from scipy import ndimage
# from skimage.transform import resize
import pickle
from numpy.fft import fftfreq, ifft, fftshift

def reverseSpectrogam(filename):
        f = misc.imread(filename, flatten=True, mode='F')

        im = np.zeros((f.shape[0]*2, f.shape[1]))
        im[:][:f.shape[0]] = f
        im[:][f.shape[0]:] = f[::-1]

        x = np.zeros(im.shape[0]*im.shape[1], dtype=np.complex64)

        for i, column in enumerate(im.T[::21]):
            signalWindow = fftshift(ifft(column))
            # plt.subplot(2, 1, 1)
            # plt.plot(column)
            # plt.subplot(2, 1, 2)
            # plt.plot(fftshift(signalWindow))
            # plt.show()
            x[i*im.shape[0]:(i+1)*im.shape[0]] = signalWindow

        # Normalize it to [-1,1]
        x = x/max(abs(x))

        return x

def savePulse(filename, pulse):
    print("saving pulse {}: {} samples".format(filename, len(pulse)))
    with open("pulses/{}.pk".format(filename), "wb") as outfile:
        pickle.dump(pulse, outfile)

    with open("pulses/{}.bin".format(filename), "wb") as outfile:
        pulse.tofile(outfile)

if __name__ == '__main__':
    files = ['pulses/pacman.png', 'pulses/ghost.png']

    pulses = []
    for image in files:
        pulses.append(reverseSpectrogam(image))

    for i, pulse in enumerate(pulses):
        savePulse(i, pulse)
