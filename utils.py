from urllib.parse import urlparse, parse_qs
import re


def extract_video_id(url):
    """
    Extracts the YouTube video ID from different YouTube URL formats.
    """

    parsed_url = urlparse(url)

    # Standard YouTube URL
    if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
        return parse_qs(parsed_url.query).get("v", [None])[0]

    # Short YouTube URL
    elif parsed_url.hostname == "youtu.be":
        return parsed_url.path.lstrip("/")

    return None


def clean_filename(filename):
    """
    Removes invalid characters from filenames.
    """

    filename = re.sub(r'[\\/*?:"<>|]', "", filename)

    filename = filename.replace(" ", "_")

    return filename