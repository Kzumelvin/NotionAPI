"""Notion databases.

This module helps to modify Notion databases.

Authors:
    Kevin Haberl <mail@beerpongturnier.de>

"""

import requests


def queryDatabase(database_id, headers):
    url = f"https://api.notion.com/v1/databases/{database_id}/query"
    payload = {"pagesize": 100}
    response = requests.request("POST", url, json=payload, headers=headers)
    return response


