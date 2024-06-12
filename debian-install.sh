#!/bin/sh
echo "here we go!!!, hit ctrl+c now if you're not ready"
sleep 15
echo "I'm going to install screen first, you'll be glad i did"
sleep 5
apt -y install screen
sleep 5
echo "installing the bare audio work essentials"
apt -y install libasound2 pulseaudio
sleep 5 
echo "installing serial communication system"
apt -y install cutecom minicom
sleep 5
echo "installing menu driver backend"
apt -y install screen xinit xorg flwm lxterminal mc
echo "this script isn't finished, here's just what i was able to do in a matter of minutes, don't clone this git till it's ready enough, or accept the risk of using an unfinished project, thank you!"
