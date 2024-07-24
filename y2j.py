import json
import yaml
import sys

def yaml_to_json(yaml_f, json_f):
    # read yaml file
    with open(yaml_f, 'r') as f:
        data = yaml.safe_load(f)

    # convert yaml to json
    json_data = json.dumps(data, indent=4)

    # write json file
    with open(json_f, 'w') as f:
        f.write(json_data)

if __name__ == "__main__":
    #  file paths for yaml to json
    input_yaml_file = 'verify.yaml'  
    output_json_file = 'verify.json'  
    
    # convert yaml to json
    yaml_to_json(input_yaml_file, output_json_file)
    print(f"converted {input_yaml_file} to {output_json_file}")