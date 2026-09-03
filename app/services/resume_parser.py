from io import BytesIO

from pypdf import PdfReader


def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """
    Extract text from all pages of a PDF resume.
    """

    pdf_stream = BytesIO(pdf_bytes)
    reader = PdfReader(pdf_stream)

    pages_text = []

    for page in reader.pages:
        try:
            text = page.extract_text()

            if text:
                pages_text.append(text)

        except Exception:
            continue

    return "\n".join(pages_text).strip()
