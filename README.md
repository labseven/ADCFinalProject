# Wireless Transmission of Digital Data using  
ADC Fall 2017 Final Project
Marie-Caroline Fink, Adam Novotny, Jonah Spear

<img src="https://github.com/labseven/ADCFinalProject/blob/master/Report_Resources/pacman_banner.jpg" alt="Pacman Banner" width="1000" height="200">

### Overview

The goal of this project is to encode and transmit digital data in a way that the transmission signal is a human-recognizable image. Previous work includes Aphex Twin's song [Equation] which when viewed through a spectrogram looks like a human face.

<img src="https://github.com/labseven/ADCFinalProject/blob/master/Report_Resources/Equation_Aphex_Twin_Spectrogram.gif" alt="Spectrogram of Aphex Twin's Equation" width="1000" height="500">


We focused on transmitting binary data using something more innocuous, namely symbols from the game Pacman.



More conc 

Goal: Transmit art using Software Defined Radio

`sudo udevadm control --reload-rules
sudo udevadm trigger`

We are assigned `2.492GHz` to `2.494GHz` -> `2MHz bandwidth`
Okay to stay `250KHz` from edges.

1. How do we transmit our data
Using software defined radios, encode arbitrary digital data into pulses that are visually recognizable images when viewed in a spectrogram.

For Example:
0 1 0 -> Dog Cat Dog

Correlating the recieved signal with puluses of Dog and Cat will give us the bits.
