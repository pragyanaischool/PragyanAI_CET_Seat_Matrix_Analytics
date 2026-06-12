"""
exports/pdf_export.py

PDF Report Generator
"""

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.lib import colors


class PDFExporter:

    def __init__(self):

        self.styles = (
            getSampleStyleSheet()
        )

    def create_pdf(
        self,
        title,
        content,
        filepath
    ):

        doc = SimpleDocTemplate(
            filepath
        )

        elements = []

        elements.append(
            Paragraph(
                title,
                self.styles["Title"]
            )
        )

        elements.append(
            Spacer(1, 20)
        )

        elements.append(
            Paragraph(
                content,
                self.styles["BodyText"]
            )
        )

        doc.build(elements)

        return filepath

    def create_college_report(
        self,
        college_name,
        summary,
        filepath
    ):

        doc = SimpleDocTemplate(
            filepath
        )

        elements = []

        elements.append(
            Paragraph(
                f"College Report: {college_name}",
                self.styles["Title"]
            )
        )

        elements.append(
            Spacer(1, 20)
        )

        elements.append(
            Paragraph(
                summary,
                self.styles["BodyText"]
            )
        )

        doc.build(elements)

        return filepath

    def create_analytics_report(
        self,
        insights,
        filepath
    ):

        doc = SimpleDocTemplate(
            filepath
        )

        elements = []

        elements.append(
            Paragraph(
                "Analytics Report",
                self.styles["Title"]
            )
        )

        elements.append(
            Spacer(1, 20)
        )

        for item in insights:

            elements.append(
                Paragraph(
                    f"• {item}",
                    self.styles["BodyText"]
                )
            )

            elements.append(
                Spacer(1, 10)
            )

        doc.build(elements)

        return filepath
