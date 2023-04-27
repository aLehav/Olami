import PyPDF2
import requests
import os


def extract_pdf_text(url = None):
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    pdf_file = open('temp.pdf', 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)

    text = ''
    for i in range(num_pages):
        page = pdf_reader.pages[i]
        text += page.extract_text() + "\n"
    
    pdf_file.close()

    # os.remove('temp.pdf')  # add this line to delete the temporary PDF file

    return text


# myText = extract_pdf_text()
# print(myText)
