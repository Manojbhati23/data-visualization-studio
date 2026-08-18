from reportlab.pdfgen import canvas


def generate_pdf():

    pdf = canvas.Canvas(
        "report.pdf"
    )

    pdf.drawString(
        100,
        800,
        "Data Visualization Studio Report"
    )

    pdf.drawString(
        100,
        770,
        "Generated using Streamlit + Matplotlib"
    )

    pdf.save()

    return "report.pdf"