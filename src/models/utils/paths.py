import yaml

def get_cleaned_data_path():
    with open('config.yaml', 'r') as stream:
        config = yaml.safe_load(stream)

    return config['data_cleaned_dir']


def get_prepared_data_path():
    with open('config.yaml', 'r') as stream:
        config = yaml.safe_load(stream)

    return config['data_prepared_dir']