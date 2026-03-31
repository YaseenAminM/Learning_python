import PyPDF2

with open("dummy.pdf", 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    print(len(reader.pages))
    print(reader.pages[0])

    # page = reader.pages[0]
