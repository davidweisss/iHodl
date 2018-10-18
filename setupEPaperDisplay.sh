sudo apt-get install p7zip
wget https://www.waveshare.com/w/upload/1/1c/2.13inch_e-Paper_HAT-code.7z
p7zip -d 2.13inch_e-Paper_HAT-code.7z
wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.57.tar.gz
tar xvzf bcm2835-1.57.tar.gz
cd bcm2835-1.57
./configure
sudo make check
sudo make install

## Python libraries
sudo apt-get install python-dev

## RPi.GPIO
wget https://files.pythonhosted.org/packages/e2/58/6e1b775606da6439fa3fd1550e7f714ac62aa75e162eed29dbec684ecb3e/RPi.GPIO-0.6.3.tar.gz
## spidev
wget https://files.pythonhosted.org/packages/36/83/73748b6e1819b57d8e1df8090200195cdae33aaa22a49a91ded16785eedd/spidev-3.2.tar.gz

## extract
tar xvzf RPi.GPIO-0.6.3.tar.gz
tar xvzf spidev-3.2.tar.gz

## Installing the RPi.GPIO package (GPIO interface functions). Copy the installation package RPi.GPIO to your RPi board, and unzip it. Enter the unzipped file under the terminal, and run the following command to install the library:
cd RPi.GPIO-0.6.3
sudo python setup.py install
cd ..
## Run the following command to install the library smbus (I2C interface functions)
sudo apt-get install python-smbus -y
## Run the following command to install the library serial, which contains UART interface functions
sudo apt-get install python-serial
## Installing the library spidev (SPI functions). Copy the installation package spidev to your RPi board, and unzip it. Enter the unzip file under the terminal, and run the following command to install the library:
cd spidev-3.2
sudo python setup.py install
cd ..
## Run the following command to install the Python imaging library
sudo apt-get install python-imaging -y
