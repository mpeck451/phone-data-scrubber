import metadata
import scrub
import csv
from datetime import datetime

# 1 - Initialize Variables
print("Script Start...")
formatted_time = datetime.now().strftime("%m-%d-%Y-%H%M%S")
initial_data = {}
processed_data = {}
fields = []
phone_fields = ['OFFICE #', 'ALTERNATE #', 'HOME #', 'CELL #']
meta_data = {
    'initial_meta_data': [],
    'result_meta_data': [],
}

# 2 - Read Initial Data
with open('initial-data.txt', 'r', newline='') as initial_data_file:
    file_reader = csv.DictReader(initial_data_file, delimiter='\t')
    initial_data = list(file_reader)
fields = list(initial_data)[0].keys()

# 3 - Capture Initial Metadata
for field in phone_fields:
    meta_data['initial_meta_data'].append(metadata.capture_phone_metadata(initial_data, field))

#Generate Initial Metadata Log
with open(f"log-{formatted_time}.txt", 'w') as log_file:
    log_file.writelines(f"Log {formatted_time}\n--------------------\n####################\nINITIAL DATA SOURCE REPORT\n####################\n")
    for object in list(meta_data['initial_meta_data']):
        for label, datum in object.items():
            #print(f"{label}: {datum}")
            log_file.writelines(f"{label}: {datum} \n")
        log_file.writelines("--------------------\n")

# 4 - Clean Phone Data
processed_data = initial_data
for field in phone_fields:
    for listing in processed_data:
        listing[field] = str(scrub.scrub_phone_data(listing[field]))

# 5 - Write Result File
with open(f"result-data-{formatted_time}.tsv", 'w', newline="") as result_file:
    result_writer = csv.DictWriter(result_file, delimiter='\t', fieldnames=fields)
    result_writer.writeheader()
    for listing in processed_data:
        result_writer.writerow(listing)

# 6 - Capture Result Metadata
for field in phone_fields:
    meta_data['result_meta_data'].append(metadata.capture_phone_metadata(processed_data, field))

# 7 - Generate Result Metadata Log
with open(f"log-{formatted_time}.txt", 'a') as log_file:
    log_file.writelines(f"####################\nRESULT DATA SOURCE REPORT\n####################\n")
    for object in list(meta_data['result_meta_data']):
        for label, datum in object.items():
            #print(f"{label}: {datum}")
            log_file.writelines(f"{label}: {datum} \n")
        log_file.writelines("--------------------\n")

print(meta_data)

# 8 -Finalize
print("...Script End")