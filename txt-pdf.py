from fpdf import FPDF
import os

# save FPDF() class into
# a variable pdf
pdf = FPDF()

# Add a page
pdf.add_page()

# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size=15)

# open the text file in read mode
f = open("Multiple and Submultiple,Transformations.pptx", "r")


# insert the texts in pdf
for x in f:
    pdf.cell(200, 10, txt=x, ln=1, align='C')

# save the pdf with name .pdf
pdf.output("myg.pdf")
