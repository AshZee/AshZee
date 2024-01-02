#!/bin/sh
florence &
sleep 0.5
florence hide
nitrogen --restore &
compfy &
redshift -l 32.6609:-97.0342 &
dunst &
NetworkManager &
nm-applet &
blueman-applet &
pa-applet &
fusuma -d &
conky &
/home/ash/.config/conky/now-clocking/start.sh &
# birdtray &
# flameshot &
xscreensaver --no-splash &
alttab -t 96x96 -i 96x48 -s 2 -fg "white" -inact "black" -font "xft:Monteserrat-12" &
# ~/.fehbg &
