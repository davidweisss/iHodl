# iHodl

Own and control the bitcoin you hodl like a champ. This is an alternative to Coinbase for example, that hold the key for you. 

![ihodl](https://user-images.githubusercontent.com/1084645/46902779-7e73c780-cecb-11e8-84c6-b250f6e13a66.jpeg)
This device runs the Bitcoin Core software implementation of the Bitcoin protocol and uses it disconnected and offline to generate new-to-the-universe bitcoin keys: private key, and (deducible from private key) public key, aka bitcoin wallet address.

It runs on a standard linux distribution (Raspbian Lite, ie CLI / non-GUI).

It runs on standard hardware:
- Raspberry pi Zero https://www.raspberrypi.org/products/raspberry-pi-zero/
- Waveshare 2.13inch e-Paper HAT https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT
- Kingston micro SD card to boot up the device (any will do, I have better results with those optimized to run apps on phones.)

The cost of the parts less than $30.

## Code functionalities
- Download bitcoin source, ... install, then disconnect
- Create wallet and output key, then erase wallet and keys
- Output to e-paper display

## Background
Great feedback from Twitter friends on a simple, open, and cheap, do-it-yourself solution for bitcoin hodling where you exclusively own and control your own keys. [iHodl original design concept](https://twitter.com/davidweisss/status/1047489532130672640)

This is part of a more comprehensive bitcoin cold storage and offline signature process running an air-gapped bitcoin node and a full internet connected node. [Secure enterprise bitcoin self-management solution](https://github.com/davidweisss/Cold_storage "Cold storage and offline signature process running an air-gapped bitcoin node and a full internet connected node.")

Which in turn is part of a long timeframe effort to create a new individual-owned data-driven economic health network that uses bitcoin to transact [DNA\\/ID](https://dnavid.com). And store your DNA in your full node. Why not?
