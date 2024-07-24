import json
import yaml

def json_to_yaml(json_f, yaml_f):
    # read json file
    with open(json_f, 'r') as f:
        data = json.load(f)

    # convert json to yaml
    yaml_data = yaml.dump(data, default_flow_style=False)

    # write yaml file
    with open(yaml_f, 'w') as f:
        f.write(yaml_data)

if __name__ == "__main__":
    #  file paths
    input_json_file = 'donuts.json' 
    output_yaml_file = 'donuts.yaml'  
    
    # convert
    json_to_yaml(input_json_file, output_yaml_file)
    print(f"converted {input_json_file} to {output_yaml_file}")
