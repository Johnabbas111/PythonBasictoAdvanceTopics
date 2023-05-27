#write a program to manupulate pdf using pyPDF your program should be able to merge multiple pdf files into single pdf you are welcome to add more functionality
from pyPDF2 import PdfWriter
import os
merger = PdfWriter()
files=[file for file in os.listdir() if file.endswith(".pdf")]
for pdf in files:
  merger.append(pdf)
merger.write("merged-pdf.pdf")
merger.close()
  
  
