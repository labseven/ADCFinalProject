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

Our encoding scheme turns a sequence of bits into a sequence of pulses, which can then be turned back into bits after transmission using a cross correlation function.

# Insert picture of 0s and 1s translated to symbols here

### Transmission

To transmit an image, first we duplicate it along the X axis so that it's signal will be completely real.

<img src="https://github.com/labseven/ADCFinalProject/blob/master/Report_Resources/duplicated_image.png" alt="Pacman Duplicated">

Slices of this image are then passed through an inverse fourier transform. 3 slices here are plotted for clarity, although in reality many more are used to get a higher resolution. The same slices above from above are plotted below on one axis (notice x axis is the same). Since the image is of uniform color, the slices show up as modulated low pass filters, so the IFFT of each slice is a sinc multiplied with a cosine.  

<img src="https://github.com/labseven/ADCFinalProject/blob/master/Report_Resources/Slices.png" alt="Pacman Duplicated">


### Huffman Coding
We implemented [Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding) to compress text messages. Huffman encoding creates an optimal coding scheme, by analyzing the order of occurrence of symbols. We trained our tree with [hipster ipsum](https://hipsum.co/), to get a similar symbol frequency to what we (being millenials) want to send.

This compression compensates slightly for our slow symbol rate.

## Implementation details
Huffman coding creates a binary tree from bottom-up to be provably optimal.

First we define a simple binary tree class, which holds a parent, left and right nodes, and (optionally) data.

To generate a Huffman tree, first calculate the probability distribution of our symbols using the Counter library.
Next, create a leaf for each symbol. The parameters of each leaf are as follows:
```
weight = probability of the symbol
data   = symbol
```

Next, sort the list by weight. Pop the two lowest weighted nodes and create a new parent node for them. The new node has the following properties:
```
right = lowest weight node
left  = second lowest weight node
weight = sum of the two children
```
Insert this new node into a second list.
Repeat this process of connecting the two lowest weighted nodes (looking at the end of both lists) with a new node, until one node remains. This is the root of the Huffman tree.
>Note: our implementation does not use two buffers. It resorts the buffer every time. This is not optimal, but the speed loss in unnoticeable.

To make encoding easier, we generate a dictionary of symbols to code with a depth first search of the tree, given only the root. Moving to the left node adds a `1` to the code and moving to the right adds a `0` to the code. To encode a message, we iterate through the characters in the message and append the code for each symbol to a bitstream.

To decode a bitstream, we traverse the tree (moving left for `1` and right for `0`) until we hit a leaf. We append that leaf's symbol to the output string, and repeat the process until we run out of bits.

### Packetization

To improve reliability, we [packetize](https://en.wikipedia.org/wiki/Network_packet) our bitstream before sending.

We chunk up the bitstream into bytes (8 bits). Then we append a known header [1, 0].

We add a parity bit to the end for detecting errors. A [parity bit](https://en.wikipedia.org/wiki/Parity_bit) makes makes the sum of the packet even. This way, we can detect one bit flip. Unfortunately, we have no way to communicate back to the transmitter, so we have to accept the data loss and move on with our lives.

This makes our packets 11 bits long.
