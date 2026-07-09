import requests
from utils import extract_video_id


def get_video_title(url):
    """
    Returns the YouTube video's title.
    """

    video_id = extract_video_id(url)

    endpoint = (
        f"https://www.youtube.com/oembed"
        f"?url=https://www.youtube.com/watch?v={video_id}&format=json"
    )

    response = requests.get(endpoint, timeout=10)

    data = response.json()

    return data["title"]