from configparser import ConfigParser


# class ConfigReader:
def read_config(key, section):
    parse = ConfigParser()
    parse.read("../ConfigurationData/conf.ini")
    print(parse.get(key, section))
    return parse.get(key, section)


# print(read_config("baseUrl", "url"))