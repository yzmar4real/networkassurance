# NetworkAssurance
This repository captures 

Python Code that allows Security Engineers to audit their palo alto firewalls, specifically checking through the rules and policies for objects that are not in use. This is particularly helpful in instances where brownfield environments are onboarded, or cybersecurity audits are carried out to ensure that objects are well-organized and comply with specific standards. 

# Use-Case Description 

The thoughts around the use-case for this project is built around CyberSecurity Engineers encountering a brownfield environment and have to audit & assess existing policies, objects, etc. having an automated way of extracting, filtering, comparing and documenting the results of objects (e.g tags, service ports, applications and in this case IP-Objects), goes a long way in providing a solid base to start from. 

# Contacts

Oluyemi Oshunkoya (yemi_o@outlook.com)

# Prerequisites

Before running this tool, you need to have the following:

Python 3.x installed on your system
The requests library installed. You can install it using the following command: pip install requests
Pandas library installed. You can install it using the following command: pip install pandas
Access to a Palo Alto firewall with API access enabled. In this code,testing was done with Palo Alto Firewalls running v10.0 Code in standalone mode.

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

