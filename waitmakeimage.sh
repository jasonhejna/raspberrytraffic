#!/bin/sh
sleep 140s
DISPLAY=:0.0 XAUTHORITY=/home/pi/.Xauthority sudo python makeimage.py
exit 0
