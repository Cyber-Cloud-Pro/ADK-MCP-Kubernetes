#!/bin/bash

echo " Creating a Python Virtual Env "
sudo apt install python3.12-venv -y
python3 -m venv .venv
source .venv/bin/activate
echo "-----Installing the requirements -----"
pip install -r req.txt

source .venv/bin/activate
adk web
