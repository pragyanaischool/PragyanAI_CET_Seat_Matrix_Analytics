"""
extraction/pdf_parser.py

PDF Text Extraction
"""

import fitz
import pdfplumber
from pathlib import Path


class PDFParser:

    def __init__(self):
        pass

    def extract_text_pymupdf(
        self,
        pdf_path
    ):

        text = ""

        doc = fitz.open(pdf_path)

        for page in doc:

            text += page.get_text()

            text += "\n"

        doc.close()

        return text

    def extract_text_pdfplumber(
        self,
        pdf_path
    ):

        text = ""

        with pdfplumber.open(pdf_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:

                    text += page_text

                    text += "\n"

        return text

    def extract_text(
        self,
        pdf_path
    ):

        try:

            return self.extract_text_pdfplumber(
                pdf_path
            )

        except Exception:

            return self.extract_text_pymupdf(
                pdf_path
            )

    def get_page_count(
        self,
        pdf_path
    ):

        doc = fitz.open(pdf_path)

        pages = len(doc)

        doc.close()

        return pages
