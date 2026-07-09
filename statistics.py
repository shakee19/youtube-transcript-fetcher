def transcript_statistics(text):
    """
    Calculate transcript statistics.
    """

    words = text.split()

    word_count = len(words)

    character_count = len(text)

    line_count = len(text.splitlines())

    reading_time = max(1, round(word_count / 200))

    return {
        "words": word_count,
        "characters": character_count,
        "lines": line_count,
        "reading_time": reading_time
    }