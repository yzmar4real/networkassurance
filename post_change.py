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

file_path = os.path.abspath('./genie.yaml')
pre_change_path = os.path.abspath('./files/arp_prechange.csv')
postchange_path = os.path.abspath('./files/arp_postchange.csv')
postchange_path_txt = os.path.abspath('./files/arp_postchange.txt')

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

    command = dev.execute

    log.info(banner("PERFORMING POST-CHANGE"))

    #import the list of IP's from the pre-change (CSV)

    pre_change_data = extract_from_csv(pre_change_path)

    ##Validate pre-change-data
    outflow = []

    # for item in pre_change_data:
    #     ip_status = process_ips(item,command)
    #     outflow.append({"IP": item, "Outcome": ip_status})

    for index, row in pre_change_data.iterrows():
        ip_val = row['ip']
        link_layer_address = row['link_layer_address']
        res_ip_val = process_ips(ip_val,command)

        # Append extracted data to the list
        outflow.append({'ip': ip_val, 'link_layer_address': link_layer_address, 'Output_Ping': res_ip_val})
    
    post_change_arp = dev.execute('show arp')

write_to_csv(postchange_path,outflow)
write_to_text(postchange_path_txt,post_change_arp)

# Presenting the data in a table
table = PrettyTable()
table.field_names = ["IP Address", "Link Layer Address", "Output Ping"]

for item in outflow:
    table.add_row([item['ip'], item['link_layer_address'], item['Output_Ping']])

print("\nData in Table Format:\n", table)
