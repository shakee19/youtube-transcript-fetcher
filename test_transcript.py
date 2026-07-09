from transcript import fetch_transcript, transcript_to_text
from file_handler import save_as_text, save_as_json

video_id = "dQw4w9WgXcQ"

transcript = fetch_transcript(video_id)

text = transcript_to_text(transcript)

save_as_text(text)

save_as_json(transcript)

print("✅ Transcript saved successfully!")