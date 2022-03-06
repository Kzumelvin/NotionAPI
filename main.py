from configparser import ConfigParser
from youtube import youtube as yt

# ConfigParser
config = ConfigParser()
config.read("secret.ini")
database_id = config.get('NOTION', 'database_id')
secret = config.get('NOTION', 'secret')

print(database_id, secret)
print(yt.getVideoId("https://www.youtube.com/watch?v=Mygh_puOUD4"))