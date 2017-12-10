# Installation:

```
sudo add-apt-repository ppa:ettusresearch/uhd
sudo apt-get update
sudo apt-get install libuhd-dev libuhd003 uhd-host gnuradio

gnuradio-config-info --version
cp uhd-usrp.rules /etc/udev/rules.d/

sudo uhd_images_downloader
uhd_usrp_probe
```

Now the usrp should show up and connect.

binaryRead.py can read the binary file
listenTo2.4GHz.py reads 2.4GHz


```
sudo udevadm control --reload-rules
sudo udevadm trigger
```

We are assigned `2.492GHz` to `2.494GHz` -> `2MHz bandwidth`
Okay to stay `250KHz` from edges.


##

Writing a np array to bytes:
`with open("sendbytes", "wb") as outfile:
 sigOut.tofile(outfile)`

Binary read:
`f = scipy.fromfile(open("inFile"), dtype=scipy.complex64)`
