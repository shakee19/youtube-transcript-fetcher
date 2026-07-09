class InvalidURLException(Exception):
    """Raised when an invalid YouTube URL is provided."""
    pass


class TranscriptNotFoundException(Exception):
    """Raised when transcript is unavailable."""
    pass


class SaveFileException(Exception):
    """Raised when saving a file fails."""
    pass