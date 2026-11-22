"""
generate_submission_docx.py
Compiles the official 50-Question Applied Business Analytics Final Submission Document into Microsoft Word (.docx).
Output: Applied_Business_Analytics_Final_Submission.docx
"""

import os
import re
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FIGURES_DIR = os.path.join(BASE_DIR, "figures")
OUT_DOCX = os.path.join(BASE_DIR, "Applied_Business_Analytics_Final_Submission.docx")
MD_SRC = os.path.join(BASE_DIR, "FINAL_SUBMISSION_50_QUESTIONS.md")


def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>'))


def build_docx():
    doc = docx.Document()

    # Margins
    for sec in doc.sections:
        sec.top_margin = Inches(1.0)
        sec.bottom_margin = Inches(1.0)
        sec.left_margin = Inches(1.0)
        sec.right_margin = Inches(1.0)

    # Styles
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    normal_style.paragraph_format.line_spacing = 1.15
    normal_style.paragraph_format.space_after = Pt(4)

    # Title Block
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_p.paragraph_format.space_before = Pt(12)
    title_p.paragraph_format.space_after = Pt(8)
    run_t = title_p.add_run("Applied Business Analytics — Applied Statistics Interview Grind\nFinal Capstone Submission (50 Core Solutions)")
    run_t.font.size = Pt(18)
    run_t.font.bold = True
    run_t.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

    sub_p = doc.add_paragraph()
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub_p.paragraph_format.space_after = Pt(12)
    run_s = sub_p.add_run("Candidate: Jignesh Kumar | Track: Data Science & Agentic AI (Module 1)\nWoolf University & Vishleshan I-Hub, IIT Patna (AlmaBetter Track) | November 2026")
    run_s.font.size = Pt(10)
    run_s.font.italic = True
    run_s.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

    # Read and parse FINAL_SUBMISSION_50_QUESTIONS.md
    with open(MD_SRC, "r", encoding="utf-8") as f:
        lines = f.readlines()

    current_p = None
    in_code = False
    code_lines = []

    for line in lines[30:]:  # Skip top header since we added formatted title block
        line_s = line.strip()

        if line_s.startswith("```"):
            in_code = not in_code
            if not in_code and code_lines:
                cp = doc.add_paragraph()
                cp.paragraph_format.left_indent = Inches(0.4)
                cp.paragraph_format.right_indent = Inches(0.4)
                cp.paragraph_format.space_after = Pt(6)
                r = cp.add_run("\n".join(code_lines))
                r.font.name = "Courier New"
                r.font.size = Pt(9)
                code_lines = []
            continue

        if in_code:
            code_lines.append(line.rstrip())
            continue

        if not line_s:
            continue

        if line_s.startswith("### 📁 Domain:"):
            h = doc.add_paragraph()
            h.paragraph_format.space_before = Pt(14)
            h.paragraph_format.space_after = Pt(4)
            r = h.add_run(line_s.replace("#", "").strip())
            r.font.size = Pt(14)
            r.font.bold = True
            r.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

        elif line_s.startswith("#### Question"):
            h = doc.add_paragraph()
            h.paragraph_format.space_before = Pt(10)
            h.paragraph_format.space_after = Pt(4)
            r = h.add_run(line_s.replace("#", "").strip())
            r.font.size = Pt(12)
            r.font.bold = True
            r.font.color.rgb = RGBColor(0x2B, 0x5C, 0x8F)

        elif line_s.startswith(">"):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.3)
            p.paragraph_format.space_after = Pt(4)
            r = p.add_run(line_s.replace(">", "").strip())
            r.font.italic = True
            r.font.color.rgb = RGBColor(0x33, 0x33, 0x33)

        elif line_s.startswith("- ") or line_s.startswith("* "):
            p = doc.add_paragraph(style='List Bullet')
            p.paragraph_format.space_after = Pt(3)
            p.add_run(line_s[2:].strip())

        elif line_s.startswith("---"):
            continue

        elif "|" in line_s:
            # Skip markdown table borders
            if "---" in line_s:
                continue
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.2)
            p.add_run(line_s)
        else:
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(4)
            p.add_run(line_s)

    doc.save(OUT_DOCX)
    print(f"Generated Word document: {OUT_DOCX}")


if __name__ == "__main__":
    build_docx()
