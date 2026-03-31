import PyPDF2

with open("dummy.pdf", 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    print(len(reader.pages))

    page = reader.pages[0]
    rotate = page.rotate(90)
    print(rotate)

    write = PyPDF2.PdfWriter()        # ✅ was PdfFileWriter
    write.add_page(rotate)
    with open("tilt.pdf", "wb") as new_file:
        write.write(new_file)
