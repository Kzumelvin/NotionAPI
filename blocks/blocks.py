"""Notion blocks.

This module helps to modify Notion blocks.

Authors:
    Kevin Haberl <mail@beerpongturnier.de>

"""

import requests

def retrieveBlock(block_id, headers):
    url = f"https://api.notion.com/v1/blocks/{block_id}"
    response = requests.request("GET", url=url, headers=headers)
    return response

def appendBlockChildren(block_id, headers, *payloads):
    """Appends a item to a block or a page.

        The block ID of a page is the page ID
    	payloads have the following structure:
    	{
          "object": "block", << always necessary
          "type": "paragraph", << the object typ to be appended
          "paragraph": { << the defintion of the object
            "text": [{
                "type": "text",
                "text":
                    {
                        "content": "– Notion API Team",
                        "link": {
                            "type": "url",
                            "url": "https://twitter.com/NotionAPI"
                            }
                    }
                }]
        }

    more to https://developers.notion.com/reference
    """
    url = f"https://api.notion.com/v1/blocks/{block_id}/children"
    payload_items = []
    for item in payloads:
        payload_items.append(item)
    payload = {
        "children": payload_items
    }
    response = requests.request("PATCH", url, json=payload, headers=headers)
    return response