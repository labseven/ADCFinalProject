# Wireless Transmission of Digital Data using  
ADC Fall 2017 Final Project
Marie-Caroline Fink, Adam Novotny, Jonah Spear

<img src="https://github.com/labseven/ADCFinalProject/blob/master/Report_Resources/pacman_banner.jpg" alt="Pacman Banner" width="1000" height="200">

## Overview

The goal of this project was to transmit binary data using a signal that looks like a game of Pacman. We were ultimately successful in transmitting simple binary data, although our transmission times were quite slow given the constraints of our method.

# Insert figure here showing transmission/results

## Background

The goal of this project was to encode and transmit digital data in a way that the transmission signal is human-recognizable.

How does this work? A spectrogram is a graph which displays frequencies of a signal on the y axis and transmission time along the x axis. By varying the signal precisely, one can draw images in this way. This has been used to embed images in songs, as shown below (Aphex Twin's Equation).

<img src="https://github.com/labseven/ADCFinalProject/blob/master/Report_Resources/Equation_Aphex_Twin_Spectrogram.gif" alt="Spectrogram of Aphex Twin's Equation" width="1000" height="500">

We focused on transmitting binary data using something more innocuous, namely symbols from the game Pacman.

## Methods


### Huffman Coding
We implemented [Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding) to compress text messages. Huffman encoding creates an optimal encoding tree, by analyzing the order of occurrence of symbols. We trained our tree with [hipster ipsum](https://hipsum.co/), to get a similar symbol frequency to what we (being millenials) want to send.

This compression compensates slightly for our slow symbol rate.



More conc

Goal: Transmit art using Software Defined Radio



1. How do we transmit our data
Using software defined radios, encode arbitrary digital data into pulses that are visually recognizable images when viewed in a spectrogram.

For Example:
0 1 0 -> Dog Cat Dog

Correlating the recieved signal with puluses of Dog and Cat will give us the bits.
