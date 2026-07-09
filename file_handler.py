import json
import os
from config import OUTPUT_FOLDER


os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def save_as_text(text, filename):

    path = os.path.join(OUTPUT_FOLDER, filename + ".txt")

    with open(path, "w", encoding="utf-8") as file:

        file.write(text)


def save_as_json(transcript, filename):

    path = os.path.join(OUTPUT_FOLDER, filename + ".json")

    data = []

    for snippet in transcript.snippets:

        data.append({
            "text": snippet.text,
            "start": snippet.start,
            "duration": snippet.duration
        })

    with open(path, "w", encoding="utf-8") as file:

        json.dump(data, file, indent=4, ensure_ascii=False)