sudo apt-get install p7zip
wget https://www.waveshare.com/w/upload/1/1c/2.13inch_e-Paper_HAT-code.7z
p7zip -d 2.13inch_e-Paper_HAT-code.7z
wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.57.tar.gz
tar xvzf bcm2835-1.57.tar.gz
cd bcm2835-1.57
./configure
sudo make check
sudo make install
