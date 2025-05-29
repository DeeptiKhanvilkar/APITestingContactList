from configparser import ConfigParser


# class ConfigReader:
def read_config(section, key):
    parse = ConfigParser()
    parse.read("../ConfigurationData/conf.ini")
    print(parse.get(section, key))
    return parse.get(section, key)


# print(read_config("baseUrl", "url"))