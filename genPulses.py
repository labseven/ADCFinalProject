import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from scipy import signal
from scipy import ndimage
# from skimage.transform import resize
import pickle
from numpy.fft import fftfreq, ifft, fftshift


def reverseSpectrogam(filename, downsample=0.05):
        f = misc.imread(filename, flatten=True)
        im = np.zeros((f.shape[0]*2, f.shape[1]))
        im[:][:f.shape[0]] = f
        im[:][f.shape[0]:] = f[::-1]
        im_ds = misc.imresize(im, downsample)
        print(im_ds.shape)

        x = np.zeros((im_ds.shape[0]*im_ds.shape[1]), dtype=np.complex64)

        for i, column in enumerate(im_ds.T):
            signalWindow = fftshift(ifft(column))
            # plt.subplot(2, 1, 1)
            # plt.plot(column)
            # plt.subplot(2, 1, 2)
            # plt.plot(fftshift(signalWindow))
            # plt.show()
            x[i*im_ds.shape[0]:(i+1)*im_ds.shape[0]] = signalWindow

        # Normalize it to [-1,1]
        x = x/max(abs(x))
        f, t, Sxx = signal.spectrogram(x, 4e6)
        plt.pcolormesh(t, f, Sxx)
        plt.show()

        return x

def savePulse(filename, pulse):
    print("saving pulse {}: {} samples".format(filename, len(pulse)))
    with open("pulses/{}.pk".format(filename), "wb") as outfile:
        pickle.dump(pulse, outfile)

    with open("pulses/{}.bin".format(filename), "wb") as outfile:
        pulse.tofile(outfile)

def showSpectrogram(pulse, fs=320e3):
    f, t, Sxx = signal.spectrogram(pulse, fs=fs)
    # Divide by 1e6 because we are showing Mhz
    plt.pcolormesh(t, f/1e6, Sxx)
    plt.ylabel('Frequency [MHz]')
    plt.xlabel('Time [sec]')
    plt.show()

if __name__ == '__main__':
    files = ['pulses/pacman.png', 'pulses/ghost.png']

    pulses = []
    for image in files:
        pulses.append(reverseSpectrogam(image))

    for i, pulse in enumerate(pulses):
        savePulse(i, pulse)

    # for pulse in pulses:
    #     showSpectrogram(pulse)
