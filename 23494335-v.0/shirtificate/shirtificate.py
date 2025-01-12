from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "", 32)
        self.cell(0, 40, "CS50 Shirtificate", align = 'C')

def main():
    name = input("Name: ")
    pdf = PDF()
    pdf.add_page()
    pdf.ln()
    pdf.image("shirtificate.png", x="C", w=200)
    pdf.set_y(-180)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "", 20)
    pdf.cell(0, 10, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")

main()
