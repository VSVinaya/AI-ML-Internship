print("Read a PDF Using PyPDF2")
from PyPDF2 import PdfReader
reader = PdfReader("sample.pdf")
text = ""
for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
        text += page_text
print(text)



