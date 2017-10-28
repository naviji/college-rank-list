#!/bin/sh
sudo apt-get update
sudo apt-get install python-pip
pip install --upgrade pip
while read p; do
	pip3 install $p
done < requirements.txt
