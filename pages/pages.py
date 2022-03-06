"""Notion pages.

This module helps to modify Notion pages.

Authors:
    Kevin Haberl <mail@beerpongturnier.de>

"""

import requests

def retrievePage(page_id, headers):
    url = f"https://api.notion.com/v1/pages/{page_id}"

