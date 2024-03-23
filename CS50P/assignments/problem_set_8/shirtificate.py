"""
from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica",'b',  30)
pdf.cell(210, 50, "CS50 Shirtificate", align = 'c')
image = "./shirtificate.png"
pdf.image(image, x = 60, y = 60, w = 100)
pdf.set_text_color(255,255,255)
pdf.cell(210, 150, "John Harvard took CS50", align = 'c')
pdf.output("shirtificate.pdf")

"""

from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica",'b',  30)
        self._pdf.cell(0, 60, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
        self._pdf.image("./shirtificate.png", w = self._pdf.epw)
        self._pdf.set_font_size(30)
        self._pdf.set_text_color(255,255,255)
        self._pdf.text(x=47.5, y = 140, txt = f"{name} took CS50")

    def save(self, name):
        self._pdf.output(name)

name = input("Name: ")
pdf = PDF(name)
pdf.save("shirtificate.pdf")