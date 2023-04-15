import PyPDF2
import requests
import os


def extract_pdf_text(url = "https://newspapers.uflib.ufl.edu/UF00028290/04444/pdf"):
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    pdf_file = open('temp.pdf', 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    num_pages = pdf_reader.numPages

    text = ''
    for i in range(num_pages):
        page = pdf_reader.getPage(i)
        text += page.extractText()
    
    pdf_file.close()

    # os.remove('temp.pdf')  # add this line to delete the temporary PDF file

    return text


myText = extract_pdf_text()
print(myText)
