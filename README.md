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
1. Run the Main.py file using the command - python Main.py

2. Follow the prompts to enter the firewall IP address, username, and password

3. The tool will retrieve the firewall objects and security rules and policies, compare them, and output the used and non-used objects as json files and a excel sheet. 

# Functions
This tool consists of the following functions:

1. get_api_key(fw_ip, fw_user, fw_pass): Retrieves the API key for the specified firewall IP address, username, and password.
2. get_object_only(api_key, fw_ip): Retrieves a list of firewall objects for the specified API key and firewall IP address.
3. get_object_details(api_key,fw_ip): Retrieves a detailed list of firewall objects (IP address & Object Name) for the specified API key and firewall IP address.  
4. get_sec_rules(fw_ip, api_key): Retrieves a list of firewall security rules and policies for the specified firewall IP address and API key.
5. get_firewall_info(): Prompts the user to enter the firewall IP address, username, and password.
6. compare_lists(list1, list2): Compares two lists and returns the matching and non-matching values.

