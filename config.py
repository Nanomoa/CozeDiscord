import yaml


def load_config():
    try:
        with open('./config.yaml', 'r') as stream:
            config_dict = yaml.safe_load(stream)
        return Config(config_dict)
    except yaml.YAMLError as exc:
        print(f"发生错误: {exc}")
        return None


class Config:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            if isinstance(v, dict):
                self.__dict__[k] = Config(v)
            else:
                self.__dict__[k] = v
