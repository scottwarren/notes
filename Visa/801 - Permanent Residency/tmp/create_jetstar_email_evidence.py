from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


OUT = (
    "/Users/scottwarren/projects/notes/Personal/Visa/801 - Permanent Residency/"
    "Prepared Documents/Evidence Gathered/Travel Evidence - Kristina Warren - "
    "Bali Return Jetstar Confirmation - 2025-10-10 to 2025-10-11 - "
    "WaKr-2631-801-3.pdf"
)

styles = getSampleStyleSheet()
body = ParagraphStyle(
    "body", parent=styles["BodyText"], fontName="Helvetica", fontSize=10,
    leading=14, textColor=colors.HexColor("#222222"), spaceAfter=5
)
small = ParagraphStyle(
    "small", parent=body, fontSize=8.5, leading=11, textColor=colors.HexColor("#555555")
)
small_white = ParagraphStyle(
    "small_white", parent=small, textColor=colors.white, fontName="Helvetica-Bold"
)
title = ParagraphStyle(
    "title", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=17,
    leading=21, textColor=colors.HexColor("#222222"), alignment=TA_LEFT, spaceAfter=8
)
section = ParagraphStyle(
    "section", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=12,
    leading=15, textColor=colors.HexColor("#222222"), spaceBefore=8, spaceAfter=5
)
hero = ParagraphStyle(
    "hero", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=18,
    leading=22, textColor=colors.white, alignment=TA_CENTER
)


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#D0D0D0"))
    canvas.line(20 * mm, 15 * mm, 190 * mm, 15 * mm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#666666"))
    canvas.drawString(20 * mm, 10 * mm, "Client reference: WaKr-2631-801-3")
    canvas.drawRightString(190 * mm, 10 * mm, f"Page {doc.page}")
    canvas.restoreState()


doc = SimpleDocTemplate(
    OUT, pagesize=A4, rightMargin=20 * mm, leftMargin=20 * mm,
    topMargin=18 * mm, bottomMargin=22 * mm,
    title="Jetstar Bali Return Flight Confirmation - Kristina Warren",
    author="Scott Warren",
)

story = []
story.append(Paragraph("Email evidence — Jetstar return flight confirmation", title))
story.append(Paragraph(
    "This document is a legible reproduction of the flight details in the Jetstar confirmation "
    "that Kristina Warren forwarded to Scott Warren on 18 October 2026. The original Jetstar "
    "email was dated 9 September 2025.", body
))

headers = [
    [Paragraph("Forwarded by", small), Paragraph("Kristina Warren &lt;kristinawarren13@gmail.com&gt;", body)],
    [Paragraph("Forwarded to", small), Paragraph("Scott Warren &lt;realscottwarren@gmail.com&gt;", body)],
    [Paragraph("Forwarded date", small), Paragraph("18 October 2026, 11:56 am AEDT", body)],
    [Paragraph("Original sender", small), Paragraph("Jetstar &lt;noreply@jetstar.com&gt;", body)],
    [Paragraph("Original email date", small), Paragraph("9 September 2025, 8:33 pm", body)],
    [Paragraph("Original subject", small), Paragraph("Jetstar Booking Confirmation Email", body)],
]
t = Table(headers, colWidths=[38 * mm, 132 * mm])
t.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#F3F3F3")),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#D6D6D6")),
    ("LEFTPADDING", (0, 0), (-1, -1), 7),
    ("RIGHTPADDING", (0, 0), (-1, -1), 7),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
]))
story.append(t)
story.append(Spacer(1, 10 * mm))

banner = Table([[Paragraph("Thanks for flying Jetstar", hero)]], colWidths=[170 * mm])
banner.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F36C21")),
    ("TOPPADDING", (0, 0), (-1, -1), 12),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
]))
story.append(banner)
story.append(Spacer(1, 5 * mm))
story.append(Paragraph("Booking reference: <b>LNFZHW</b>", section))
story.append(Paragraph("Passenger: <b>Kristina Warren</b>", body))

flight = [
    [Paragraph("Flight", small_white), Paragraph("Departing", small_white), Paragraph("Arriving", small_white)],
    [Paragraph("<b>JQ 94</b>", body),
     Paragraph("<b>DPS — Denpasar, Bali</b><br/>11:45 pm<br/>Friday 10 October 2025", body),
     Paragraph("<b>OOL — Gold Coast</b><br/>7:15 am<br/>Saturday 11 October 2025", body)],
]
ft = Table(flight, colWidths=[28 * mm, 71 * mm, 71 * mm])
ft.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#333333")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("GRID", (0, 0), (-1, -1), 0.7, colors.HexColor("#C8C8C8")),
    ("LEFTPADDING", (0, 0), (-1, -1), 9),
    ("RIGHTPADDING", (0, 0), (-1, -1), 9),
    ("TOPPADDING", (0, 0), (-1, -1), 9),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
]))
story.append(ft)
story.append(Spacer(1, 7 * mm))
story.append(Paragraph(
    "The confirmation records Kristina leaving Indonesia on 10 October 2025 and arriving in "
    "Australia on 11 October 2025.", body
))
story.append(Spacer(1, 5 * mm))
story.append(Paragraph(
    "Source note: the Jetstar confirmation was forwarded as an email body and did not include a "
    "separate itinerary PDF attachment. The identifying details above reproduce the readable "
    "information in that forwarded confirmation.", small
))

doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUT)
