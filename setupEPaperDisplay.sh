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

## Configuring the interfaces
## (Before running the API codes we provided, you should start up the corresponding core drivers of the interfaces. In the ready-to-use system image file, both I2C and SPI are set to Enable by default, but the serial port is still in the terminal debugging function mode.)

## ## Enable the I2C function. Run the following command to configure your Raspberry Pi board:
## sudo raspi-config
## ## Select Advanced Options -> I2C -> yes, to start up the I2C core driver. Then you also need to modify the configuration file. Run the following command to open the configuration file:
## sudo nano /etc/modules
## ## Add the following two lines to the configuration file
## i2c-bcm2708
## i2c-dev
## ## Press the keys Ctrl+X to exit, and input Y to save the settings. Then, reboot the module to make the settings take effect.
## ## Enable the serial function. The serial port of RPi is set to serial terminal debugging function mode by default. If you want the serial port services as a common IO, you should modify the settings on the RPi. When the terminal debugging function is disabled, you cannot access RPi board via the serial port any more. If you want to control the RPi, you may need to enable the debugging function of the serial port again.
## sudo raspi-config
## ## Select Advanced Options -> Serial. Select the option no can disable the serial debugging function. And then, the serial port can be used for serial communication. And select the option yes can enable the serial debugging function. You should reboot the module to make the settings take effect.
## ## Note: the serial port on Raspberry Pi 3 Model B is unusable, because Pin 14 and Pin 15 is connected to the on-board Bluetooth model.
## ## Start up the spi function, run the following command:
## sudo raspi-config
## ## Select Advanced Options -> I2C -> yes, to start up I2C core driver.
