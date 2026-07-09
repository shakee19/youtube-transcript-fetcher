from transcript import fetch_transcript, transcript_to_text, get_available_languages
from file_handler import save_as_json, save_as_text
from utils import extract_video_id, clean_filename
from youtube import get_video_title
from logger import log_info, log_error
from statistics import transcript_statistics
from config import APP_NAME, VERSION
from pdf_exporter import save_as_pdf

def main():

    try:

        print("=" * 60)
        print(f"        {APP_NAME}")
        print(f"            Version {VERSION}")
        print("=" * 60)

        log_info("Application Started")

        url = input("\nEnter YouTube URL: ").strip()

        video_id = extract_video_id(url)

        if not video_id:
            raise ValueError("Invalid YouTube URL")

        # -------------------------------
        # Show available transcript languages
        # -------------------------------

        print("\n🌍 Fetching available languages...")

        languages = get_available_languages(video_id)

        print("\nAvailable Languages:\n")

        for index, language in enumerate(languages, start=1):
            print(f"{index}. {language['name']} ({language['code']})")

        choice = int(input("\nChoose Language: "))

        if choice < 1 or choice > len(languages):
            raise ValueError("Invalid language selection.")

        selected_language = languages[choice - 1]

        # -------------------------------
        # Fetch video title
        # -------------------------------

        print("\n🎥 Fetching Video Title...")

        title = get_video_title(url)

        filename = clean_filename(title)

        print(f"✅ {title}")

        # -------------------------------
        # Download transcript
        # -------------------------------

        print(f"\n🌍 Downloading {selected_language['name']} Transcript...")

        transcript = fetch_transcript(
            video_id,
            selected_language["code"]
        )

        text = transcript_to_text(transcript)
        stats = transcript_statistics(text)

        save_as_text(text, filename)

        save_as_json(transcript, filename)
        save_as_pdf(text, filename)

        log_info(f"Transcript saved successfully: {filename}")

        print("\n" + "━" * 60)

        print("📊 Transcript Statistics\n")

        print(f"Words        : {stats['words']}")
        print(f"Characters   : {stats['characters']}")
        print(f"Lines        : {stats['lines']}")
        print(f"Reading Time : {stats['reading_time']} minute(s)")

        print("\n" + "━" * 60)

        print("✅ Download Successful\n")

        print("📁 Files Saved")

        print(f"✔ transcripts/{filename}.txt")
        print(f"✔ transcripts/{filename}.json")
        print(f"✔ transcripts/{filename}.pdf")

        print("\n📝 Log File")
        print("✔ logs/app.log")

        print("\n" + "━" * 60)

        print("🎉 Thank you for using YouTube Transcript Fetcher Pro!")

    except ValueError as e:

        log_error(str(e))

        print(f"\n❌ {e}")

    except Exception as e:

        log_error(str(e))

        print("\n❌ Something went wrong.")
        print(e)


if __name__ == "__main__":
    main()