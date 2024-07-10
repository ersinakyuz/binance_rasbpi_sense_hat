#!/bin/bash
if python3 --version ;
then
	pip3 install python-binance
	pip3 install requests
	sudo apt-get install python3-sense-emu sense-emu-tools
	pip3 install sense_emu
	pip3 install sense_hat

else
	echo "No Python3 executable is found. Please install Python3 first"
fi