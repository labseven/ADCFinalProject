# Installation:

`
sudo add-apt-repository ppa:ettusresearch/uhd
sudo apt-get update
sudo apt-get install libuhd-dev libuhd003 uhd-host gnuradio

gnuradio-config-info --version
cp uhd-usrp.rules /etc/udev/rules.d/

sudo uhd_images_downloader
uhd_usrp_probe
`

Now the usrp should show up and connect.


`
pip2 install scipy
`

binaryRead.py can read the binary file
listenTo2.4GHz.py reads 2.4GHz



##

Writing a np array to bytes:
`with open("sendbytes", "wb") as outfile:
 sigOut.tofile(outfile)`

Binary read:
`f = scipy.fromfile(open("inFile"), dtype=scipy.complex64)`
