from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os

from config import OUTPUT_FOLDER


def save_as_pdf(text, filename):
    """
    Save transcript as a PDF file.
    """

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    pdf_path = os.path.join(
        OUTPUT_FOLDER,
        filename + ".pdf"
    )

    document = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    story = []

    for line in text.split("\n"):

        if line.strip():

            story.append(
                Paragraph(line, styles["BodyText"])
            )

    document.build(story)