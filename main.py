from configparser import ConfigParser

# ConfigParser
config = ConfigParser()
config.read("secret.ini")
database_id = config.get('NOTION', 'database_id')
secret = config.get('NOTION', 'secret')

print(database_id, secret)