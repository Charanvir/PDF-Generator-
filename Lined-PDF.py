from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
# Pages should not be broken automatically
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    # Coordinates, x1, y1, x2, y2
    pdf.line(10, 21, 200, 21)

    pdf.ln(260)
    for i in range(2, 28):
        pdf.line(10, 21 * (i / 2), 200, 21 * (i / 2))

    pdf.set_font(family="Times", style="I", size=10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(270)
        pdf.set_font(family="Times", style="I", size=10)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
        for j in range(1, 28):
            pdf.line(10, 21 * (j / 2), 200, 21 * (j / 2))

pdf.output("lined-pdf.pdf")
