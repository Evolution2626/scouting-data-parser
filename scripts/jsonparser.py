import os
import json
import sys

if len(sys.argv) != 3:
    print("Must pass input directory and output file as parameter")
    sys.exit(1)

directory_path = sys.argv[1]
output_file_path = sys.argv[2]

output_data = []

for file_name in os.listdir(directory_path):
    if "json" in file_name:
        with open(os.path.join(directory_path, file_name), "r") as file:
            file_data = json.load(file)
            if isinstance(file_data, list):
                output_data.extend(file_data)
            else:
                output_data.append(file_data)

# Remove duplicates
output_data = list(dict.fromkeys(output_data))

with open(output_file_path, "w") as output_file:
    json.dump(output_data, output_file)
