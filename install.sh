#!/bin/bash
# Installs the required packages and sets up the machine environment
# git clone https://github.com/alexrosen45/quickposts
# cd quickposts
# ./install.sh
apt-get install python3 python3-pip
pip install -r requirements.txt

# To run this, call this command
# python3 manage.py runserver