import numpy as np
import json

file_name = 'SP_eval_data_for_practice.npy'

# Load the data with allow_pickle=True if it contains Python objects
data = np.load(f'data/{file_name}', allow_pickle=True)

# If data is a numpy array, convert it to a list format that can be serialized to JSON
if isinstance(data, np.ndarray):
    data_list = data.tolist()
else:
    data_list = data  # Assuming it's already a list or other serializable format

# Convert to JSON format
json_data = json.dumps(data_list, indent=4)

# Print JSON data
print(json_data)

# Optionally, save to a file
with open(f'data/{file_name}.json', 'w') as json_file:
    json_file.write(json_data)