"""
generate_submission_pdf.py
Generates the publication-quality PDF for Applied Business Analytics (M1_ABA):
Output: Applied_Business_Analytics_Final_Submission.pdf
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image as RLImage,
    Table,
    TableStyle,
    PageBreak,
    HRFlowable
)
from reportlab.pdfgen import canvas

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FIGURES_DIR = os.path.join(BASE_DIR, "figures")
OUT_PDF = os.path.join(BASE_DIR, "Applied_Business_Analytics_Final_Submission.pdf")
MD_SRC = os.path.join(BASE_DIR, "FINAL_SUBMISSION_50_QUESTIONS.md")


class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#555555"))

        if self._pageNumber > 1:
            self.drawString(54, 755, "Applied Business Analytics — Applied Statistics Interview Grind | Jignesh Kumar")
            self.drawRightString(612 - 54, 755, "AlmaBetter / Woolf University (M1_ABA)")
            self.setStrokeColor(colors.HexColor("#CCCCCC"))
            self.setLineWidth(0.5)
            self.line(54, 750, 612 - 54, 750)

        self.setStrokeColor(colors.HexColor("#CCCCCC"))
        self.setLineWidth(0.5)
        self.line(54, 45, 612 - 54, 45)
        self.drawString(54, 32, "Data Science & Agentic AI Track — Master's in CS (Applied AI)")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(612 - 54, 32, page_str)
        self.restoreState()


def build_pdf():
    doc = SimpleDocTemplate(
        OUT_PDF,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "DocTitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=18,
        leading=22,
        alignment=1,
        textColor=colors.HexColor("#1B365D"),
        spaceAfter=8
    )

    subtitle_style = ParagraphStyle(
        "DocSubtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        alignment=1,
        textColor=colors.HexColor("#444444"),
        spaceAfter=14
    )

    domain_style = ParagraphStyle(
        "DomainH",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#1B365D"),
        spaceBefore=12,
        spaceAfter=4,
        keepWithNext=True
    )

    q_style = ParagraphStyle(
        "QuestionH",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor("#2B5C8F"),
        spaceBefore=8,
        spaceAfter=3,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        "DocBody",
        parent=styles["Normal"],
        fontName="Times-Roman",
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor("#222222"),
        spaceAfter=4
    )

    callout_style = ParagraphStyle(
        "DocCallout",
        parent=styles["Normal"],
        fontName="Courier",
        fontSize=8.5,
        leading=11,
        leftIndent=15,
        rightIndent=15,
        textColor=colors.HexColor("#333333"),
        spaceBefore=2,
        spaceAfter=4
    )

    story = []

    story.append(Paragraph("Applied Business Analytics — Applied Statistics Interview Grind", title_style))
    story.append(Paragraph("Final Capstone Comprehensive Submission Document (50 Selected Solutions)<br/><b>Candidate:</b> Jignesh Kumar | <b>Track:</b> Data Science & Agentic AI (Module 1)<br/>Woolf University & Vishleshan I-Hub, IIT Patna (AlmaBetter Track) | November 2026", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1B365D"), spaceAfter=10))

    # Add embedded figures overview
    f1_img = os.path.join(FIGURES_DIR, "01_domain_distribution_pie.png")
    if os.path.exists(f1_img):
        story.append(RLImage(f1_img, width=360, height=270))
        story.append(Paragraph("<i>Figure 1: Distribution of 80 Questions across 6 Analytics Domains.</i>", ParagraphStyle("Cap", alignment=1, fontSize=8.5, textColor=colors.HexColor("#555555"), spaceAfter=8)))

    with open(MD_SRC, "r", encoding="utf-8") as f:
        lines = f.readlines()

    in_code = False
    code_block = []

    for line in lines[30:]:
        line_s = line.strip()

        if line_s.startswith("```"):
            in_code = not in_code
            if not in_code and code_block:
                story.append(Paragraph("<br/>".join(code_block), callout_style))
                code_block = []
            continue

        if in_code:
            code_block.append(line.rstrip().replace(" ", "&nbsp;"))
            continue

        if not line_s or line_s.startswith("---"):
            continue

        if line_s.startswith("### 📁 Domain:"):
            story.append(Paragraph(line_s.replace("#", "").strip(), domain_style))
        elif line_s.startswith("#### Question"):
            story.append(Paragraph(line_s.replace("#", "").strip(), q_style))
        elif line_s.startswith(">"):
            story.append(Paragraph(line_s.replace(">", "").strip(), callout_style))
        elif line_s.startswith("- ") or line_s.startswith("* "):
            story.append(Paragraph(f"• {line_s[2:].strip()}", body_style))
        elif "|" in line_s:
            continue  # Markdown table lines simplified for flow
        else:
            story.append(Paragraph(line_s, body_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Generated PDF: {OUT_PDF}")


if __name__ == "__main__":
    build_pdf()
