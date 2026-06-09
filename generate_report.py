from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph
)

from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate(
    "output/final_report.pdf"
)

styles = getSampleStyleSheet()

content = []

content.append(
    Paragraph(
        "Transcript Intelligence Report",
        styles["Title"]
    )
)

content.append(
    Paragraph(
        "Topic Categorization Completed",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        "Sentiment Analysis Completed",
        styles["Normal"]
    )
)

doc.build(content)

print("PDF report generated")