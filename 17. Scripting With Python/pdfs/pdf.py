import PyPDF2

# with open("dummy.pdf", 'rb') as file:
#     reader = PyPDF2.PdfReader(file)
#     print(len(reader.pages))

#     page = reader.pages[0]
#     rotate = page.rotate(90)
#     print(rotate)

#     write = PyPDF2.PdfWriter()        # ✅ was PdfFileWriter
#     write.add_page(rotate)
#     with open("tilt.pdf", "wb") as new_file:
#         write.write(new_file)


# ===================================================
with open("dummy.pdf", "rb") as f1, open("tilt.pdf", "rb") as f2:
    reader1 = PyPDF2.PdfReader(f1)
    reader2 = PyPDF2.PdfReader(f2)

    writer = PyPDF2.PdfWriter()

    # Add all pages from both files
    for page in reader1.pages:
        writer.add_page(page)

    for page in reader2.pages:
        writer.add_page(page)

    with open("combined.pdf", "wb") as output:
        writer.write(output)
