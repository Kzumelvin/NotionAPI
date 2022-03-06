from configparser import ConfigParser
from youtube import youtube as yt
from blocks import blocks

# ConfigParser
config = ConfigParser()
config.read("secret.ini")
database_id = config.get('NOTION', 'database_id')
secret = config.get('NOTION', 'secret')

headers = {
    "Accept": "application/json",
    "Notion-Version": "2022-02-22",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {secret}"
}

if __name__ == "__main__":
    print("Hallo Welt!")