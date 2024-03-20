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

modified_config =read_and_modify_router_config('network_config.yml')
write_yaml('modified_router_config.yml', modified_config)

