# ADCFinalProject
ADC Fall 2017 Final Project

Goal: Transmit art using Software Defined Radio

`sudo udevadm control --reload-rules
sudo udevadm trigger`

We are assigned `2.492GHz` to `2.494GHz`
1. How do we transmit our data
Using software defined radios, encode arbitrary digital data into pulses that are visually recognizable images when viewed in a spectrogram.

For Example:
0 1 0 -> Dog Cat Dog

Correlating the recieved signal with puluses of Dog and Cat will give us the bits.
