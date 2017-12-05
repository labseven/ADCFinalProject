import gnuradio as gr
import scipy

f = scipy.fromfile(open("inFile"), dtype=scipy.complex64)

print(f[0].real)
print(f[0].imag)
print(f[:5])
