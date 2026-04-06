from PyPDF2 import PdfFileWriter,PdfFileReader
pdfwriter= PdfFileWriter()
Pdf = PdfFileReader("1.pdf")
for page_num in range(pdf.numpages):
    pdfwriter.addpage(pdf.getpage(page_num))
passw= "123456"
pdfwriter.encrypt(passw)
with open('file3.pdf','wb') as f:
    pdfwriter.write(f)
    f.close()