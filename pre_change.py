import sys
import os
import logging
import json
import csv
import re
import pandas as pd
import pendulum as tt
from prettytable import PrettyTable
from genie.testbed import load
from pyats.log.utils import banner


def process_ips(ips,command):

    ping_result = command(f'ping {ips}')
    ping_outcomes = parse_ping_output(ping_result)

    return ping_outcomes

def write_to_text(file_name, data):
    with open(file_name, 'w') as file:
        file.write(str(data))

def parse_ping_output(output):
    # Regular expression to extract the success rate
    match = re.search(r'Success rate is (\d+)', output)
    if match:
        # Extract the success rate value
        success_rate = int(match.group(1))
        
        # Return True if success rate is 100%, otherwise False
        return 'Success' if success_rate == 100 else 'Failure'
    else:
        # If the success rate isn't found in the output, handle appropriately
        return 'Failure'
    
def write_to_json(file_name,data):
    json_data = json.dumps(data, indent=4)
    with open(file_name, 'w') as file:
        file.write(json_data)

def write_to_csv(csv_file_path,data):
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def extract_from_csv(file_path):
    try:
        # Reading CSV file using pandas
        df = pd.read_csv(file_path)
        # Extracting the 'ip' column as a list
        return df
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"

now = tt.now("GMT")
starttime = now.format("YYYY-MM-DD_HH:mm:ss")
print(starttime)

file_path = os.path.abspath('./Testbed/dime2.yaml')
csv_file_path = './files/arp_prechange.csv'


logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(message)s')
log = logging.getLogger()

log.info(banner("LOADING TESTBED FILES"))
testbed_file = load(file_path)
log.info("\nPASS: Successfully loaded testbed '{}'\n".format(testbed_file.name))

for dev in testbed_file:

    log.info(banner("CONNECTING TO THE DEVICES"))

    try:
        
        dev.connect(learn_hostname=True,init_exec_commands=[],init_config_commands=[],log_stdout=True)

    except Exception as error:
        log.info(error)

    log.info(banner("PERFORMING PRE-CHANGE"))

    # Collect the arp table details before the change 
    pre_change_data = dev.execute('show arp')
    pre_change = dev.parse('show arp')

    # Store the arp table details before the change 
    write_to_text('./files/arp_prechange.txt', pre_change_data)

    ip_list = []

    extracted_data = []

    command = dev.execute

    for interface, data in pre_change.items():

        for ip, details in data['ipv4']['neighbors'].items():
            ip_val = details['ip']
            link_layer_address = details['link_layer_address']
            res_ip_val = process_ips(ip_val,command)

            # Append extracted data to the list
            extracted_data.append({'ip': ip_val, 'link_layer_address': link_layer_address, 'Output_Ping': res_ip_val})

# Convert to JSON
json_data = json.dumps(extracted_data, indent=4)
print("JSON Data:\n", json_data)

#Save Output to JSON & CSV Files
write_to_json('./files/arp_prechange.json', extracted_data)
write_to_csv('./files/arp_prechange.csv', extracted_data)

# Presenting the data in a table
table = PrettyTable()
table.field_names = ["IP Address", "Link Layer Address", "Output Ping"]

for item in extracted_data:
    table.add_row([item['ip'], item['link_layer_address'],item['Output_Ping']])

print("\nData in Table Format:\n", table)

