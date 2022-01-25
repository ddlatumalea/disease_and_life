import yaml


def get_cleaned_data_path() -> str:
    """Returns the directory of cleaned data."""
    with open('config.yaml', 'r') as stream:
        config = yaml.safe_load(stream)

    return config['data_cleaned_dir']


def get_prepared_data_path() -> str:
    """Returns the director of prepared data."""
    with open('config.yaml', 'r') as stream:
        config = yaml.safe_load(stream)

    return config['data_prepared_dir']


def get_standardized_data_file() -> str:
    """Returns the filename of the standardized data"""
    with open('config.yaml', 'r') as stream:
        config = yaml.safe_load(stream)

    return config['standardized_data']


def get_data_path() -> str:
    with open('config.yaml', 'r') as stream:
        config = yaml.safe_load(stream)

    return config['data_dir']
