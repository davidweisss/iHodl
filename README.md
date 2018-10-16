# iHodl

Own and control the bitcoin you hodl like a champ.

The creation of a bitcoin key offline, recording it, then erasing all computer traces guarantees only you will ever have that key. You can then make a hard copy, secure it (in a safe), then deposit bitcoin = your self-managed savings bank account.

This is much safer alternative to Coinbase, for example, who hold the key for you. Much more secure than a hardware wallet. Much more secure than keeping gold in a nuclear-resistant bunker, in fact!

![ihodl](https://user-images.githubusercontent.com/1084645/46902779-7e73c780-cecb-11e8-84c6-b250f6e13a66.jpeg)
This device runs the Bitcoin Core software implementation of the Bitcoin protocol and uses it disconnected and offline to generate new-to-the-universe bitcoin keys: private key, and (deducible from private key) public key, aka bitcoin wallet address.

Runs on a standard linux distribution (Raspbian Lite, ie CLI / non-GUI).

Runs on standard hardware:
- Raspberry pi Zero https://www.raspberrypi.org/products/raspberry-pi-zero/
- Waveshare 2.13inch e-Paper HAT https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT
- Kingston micro SD card to boot up the device (any will do, I have better results with those optimized to run apps on phones.)
- Almost any micro usb phone charger will power it, can run on batteries for extra security (against snooping on electrical lines.)

Is cheap: The cost of the parts less than $30.

## Code functionalities
This repository contains instructions to create a disk image that will run embedded on the Rpi Zero.
- Download bitcoin source, ... install, then disconnect


A series of inter-dependent systemd services to:
- Erase e-paper display on power up
- Launch bitcoind and create keys with bitcoin-cli
- Output to e-paper display with manufacturer api and example code using python Image Manipulation Library
- Destroy all files potentially containing keys (on power up and after recording on e-paper)

## Background
Great feedback from Twitter friends on a simple, open, and cheap, do-it-yourself solution for bitcoin hodling where you exclusively own and control your own keys. [iHodl original design concept](https://twitter.com/davidweisss/status/1047489532130672640)

This is part of a more comprehensive bitcoin cold storage and offline signature process running an air-gapped bitcoin node and a full internet connected node. [Secure enterprise bitcoin self-management solution](https://github.com/davidweisss/Cold_storage "Cold storage and offline signature process running an air-gapped bitcoin node and a full internet connected node.")

Which in turn is part of a long timeframe effort to create a new individual-owned data-driven economic health network that uses bitcoin to transact [DNA\\/ID](https://dnavid.com). And store your DNA in your full node. Why not?
