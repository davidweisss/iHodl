#!/bin/sh
## Launching bitcoin daemon will create wallet.dat
## Launch without internet connection, blocks are not synched [3]
## Dev: screen
## bitcoind -connect=0 -nolisten 
##
f="/home/pi/iHodl/keys.txt"
newAddress=`bitcoin-cli getnewaddress` 
privateKey=`bitcoin-cli dumpprivkey $newAddress` 
echo $newAddress >> $f
echo $privateKey >> $f
## cp $f ${f}.carefulThisWasCreatedInDebugMode


## If you want to create a custom address

## for i in `seq 1 1000`; do bitcoin-cli getnewaddress|grep ^My ; done
## Or for longer strings https://twitter.com/l4rz/status/1040582046039658497

## Make a hard copy of the private key (optionally, the public key, which cam be recovered from the private key)

## Create new screen tab C^a-C^c
## Remove new wallet and wallet dump, and all the data from bitcoin on ./bitcoin
## Shred scrambles the data so that file cannot be recovered
## shred -zvu ~/.bitcoin

## Delete the whole drive securely.
## If security critical, destroy the sd card (+rpi for extreme security) physically.
