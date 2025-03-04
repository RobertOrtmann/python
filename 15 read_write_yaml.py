import yaml

def read_and_modify_router_config(file_path) :
    with open(file_path, 'r') as file:
        try:
            data = yaml.safe_load(file)
            if data['interfaces'] :
                data ['interfaces'] [0] ['ip'] = '10.10.0.1'
            return data
        except yaml.YAMLError as exc:
            print(exc)

def write_yaml(file_path, data) :
    with open(file_path, 'w' ) as file :
        yaml.dump(data, file, sort_keys=False)

modified_config =read_and_modify_router_config('15_network_config.yml')
write_yaml('15_modified_router_config.yml', modified_config)

# sort_keys=False: 
# This argument controls whether the keys in the output YAML should be sorted. 
# By setting sort_keys=False, you ensure that the keys will appear in the same order
# as they are in the original data dictionary (i.e., they won't be alphabetized).