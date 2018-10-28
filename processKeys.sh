#!/bin/bash
## Process keys for display
private=/home/pi/iHodl/private
public=/home/pi/iHodl/public
## Read
publicKey=`sed '1q;d'  /home/pi/iHodl/keys.txt`
privateKey=`sed '2q;d' /home/pi/iHodl/keys.txt`

## Fit size of display
echo ${privateKey:0:26}>> $private
echo ${privateKey:26} >> $private
echo ${publicKey:0:26}>> $public
echo ${publicKey:26}>> $public

## cp $public ${public}.carefulThisWasCreatedInDebugMode
## cp $private ${private}.carefulThisWasCreatedInDebugMode
