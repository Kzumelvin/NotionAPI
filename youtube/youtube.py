"""Youtube tools.

This module provides helpful tools for working with youtube urls and api.

Authors:
    Kevin Haberl <mail@beerpongturnier.de>

"""

def getVideoId(url):
    if "watch" in url:
        url = url.split("?v=", "?")
        return url[1]
    else:
        url = url.split("/")
        return url[3]

def getThumbnailUrl(video_url):
    video_url = getVideoId(video_url)
    thumb_url = f"https://img.youtube.com/vi/{video_url}/0.jpg"
    return thumb_url