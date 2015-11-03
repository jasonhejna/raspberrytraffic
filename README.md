# raspberrytraffic
Google Maps with Traffic on a Raspberry Pi running on a 50" TV
![alt tag](https://raw.githubusercontent.com/jasonhejna/raspberrytraffic/master/Image_rasptraffic.png)

You'll need to do a couple things...

1. Install feh image viewer http://feh.finalrewind.org/
2. Install libcec - this will turn off / on your TV through HDMI
3. Install PyQt4 with these libraries: QtCore, QtGui, and QtWebKit - used to create an image from a website
3. Download this repository into /home/pi
4. Test that everything works...

    sudo sh waitmakeimage.sh

    DISPLAY=:0.0 XAUTHORITY=/home/pi/.Xauthority sudo feh --quiet --preload -rSfilename -F -Z /home/pi/webimage.png
    
    sudo killall feh
    
5. Copy the crontab file into your crontab (command is "crontab -e")
6. Update your crontab to your desired schedule ("crontab -e").


