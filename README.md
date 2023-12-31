# NetworkAssurance
This repository highlights Python Code that enables CyberSecurity Engineers to include network assurance in their change management process. This is particularly helpful when making changes to devices (firewalls, switches) which can be disruptive in nature, in providing actual assurance that things are exactly as they were before and after the change. 

# Use-Case Description 

The thoughts around the use-case for this project is built around CyberSecurity Engineers making changes to the firewalls that pass critical traffic - e.g default gateway for servers, transit perimeter firewall for internet traffic, etc. This goes a long way in providing assurance that the environment is working as should post-change in addition to the usual confirmation from end users. 

Connectivity to the devices is done using Cisco's PYATS framework, while storing the relevant outputs in json/CSV files, and printing out the data in PrettyTable. 

# Contacts

Oluyemi Oshunkoya (yemi_o@outlook.com)

# Prerequisites

Before running this tool, you need to have the following:

Python 3.x installed on your system

Libraries: pendulum, prettytable, genie, pyats, re, csv, json, os, sys, logging, time

# Setup

1. Clone the repository

git clone https://github.com/yzmar4real/networkassurance.git

2. CD into the directory 

cd networkassurance

3. (Optional) Use the directory as a virtual environment for the project

python3 -m venv . 

4. (Optional) Start the virtual environment and install the requirements for the project

source bin/activate

# Usage

1. Edit the genie.yaml file and update the parameters with your own devices (multiple devices can be added as well)

2. Run the pre_change.py file using the command - python pre_change.py

3. The script will connect to the firewall in the genie file and check the arp table, ping the entries and store the results in a json and csv file.

4. After executing the change, run the post_change.py file using the command - python post_change.py

5. Check the files folder for the results of the code run.
   

