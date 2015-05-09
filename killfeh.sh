#!/bin/sh 
sleep 5s
DISPLAY=:0.0 XAUTHORITY=/home/pi/.Xauthority sudo ./psrch '/bin/sh -c DISPLAY=:0.0 XAUTHORITY=/home/pi/.Xauthority sudo feh --quiet --preload -rSfilename -F -Z /home/pi/webimage.png*' --kill --all --nselect 1
sleep 5s
DISPLAY=:0.0 XAUTHORITY=/home/pi/.Xauthority sudo ./psrch 'sudo feh --quiet --preload -rSfilename -F -Z /home/pi/webimage.png*' --kill --all --nselect 1
sleep 5s
DISPLAY=:0.0 sudo ./psrch 'feh --quiet --preload -rSfilename -F -Z /home/pi/webimage.png*' --kill --all --nselect 1
exit 0
