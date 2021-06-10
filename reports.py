#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, paragraph):
    styles = getSampleStyleSheet()
    styleH = styles["Heading1"]
    styleN = styles["Normal"]
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title,styleH)
    report_body = Paragraph(paragraph,styleN)
    report.build([report_title, report_body])

