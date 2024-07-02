import configparser
from pathlib import Path

cfgFile = 'petsqa.ini'
cfgFileDir = 'configurations'

config = configparser.ConfigParser()
configFlaskApp = configparser.ConfigParser()

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
CONFIG_FILE = BASE_DIR.joinpath(cfgFileDir).joinpath(cfgFile)

config.read(CONFIG_FILE)

def getPetAPIURL():
    return (config['pet']['url'])

def getStoreAPIURL():
    return (config['store']['url'])

print(getPetAPIURL())
