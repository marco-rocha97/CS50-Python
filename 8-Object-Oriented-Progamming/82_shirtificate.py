# In a file called shirtificate.py, implement a program that prompts the user for their name and outputs, using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf similar to this one for John Harvard, with these specifications:

# The orientation of the PDF should be Portrait.
# The format of the PDF should be A4, which is 210mm wide by 297mm tall.
# The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
# The shirt’s image should be centered horizontally.
# The user’s name should be on top of the shirt, in white text.
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 30)
pdf.cell(0, 30, "CS50 Shirtficate", new_x="LMARGIN", new_y="NEXT", align="C")
pdf.image("shirtificate.png", w=pdf.epw)
pdf.set_font("helvetica", "B", 20)
pdf.set_text_color(255, 255, 255)
name = input("Name: ")
pdf.text(80, 100, name + " took CS50")
pdf.output("shirtificate.pdf")