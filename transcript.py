from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
)

from exceptions import TranscriptNotFoundException


def get_available_languages(video_id):
    """
    Returns all available transcript languages for a video.
    """

    api = YouTubeTranscriptApi()

    transcript_list = api.list(video_id)

    languages = []

    for transcript in transcript_list:
        languages.append(
            {
                "name": transcript.language,
                "code": transcript.language_code,
            }
        )

    return languages


def fetch_transcript(video_id, language_code=None):
    """
    Fetch transcript in the selected language.
    """

    try:
        api = YouTubeTranscriptApi()

        if language_code:
            transcript = api.fetch(
                video_id,
                languages=[language_code]
            )
        else:
            transcript = api.fetch(video_id)

        return transcript

    except (
        NoTranscriptFound,
        TranscriptsDisabled,
        VideoUnavailable,
    ):
        raise TranscriptNotFoundException(
            "Transcript is unavailable for this video."
        )


def transcript_to_text(transcript):
    """
    Convert transcript object into plain text.
    """

    return "\n".join(
        snippet.text
        for snippet in transcript.snippets
    )