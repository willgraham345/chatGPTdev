import PyPDF2 as pdf2


def main():

    # Open the PDF file in read-binary mode

    pdf_file = open('examples/convolutional_neural_networks.pdf', 'rb')


    # Create a PDF reader object

    reader = pdf2.PdfReader(pdf_file)


    # Get the number of pages in the PDF

    num_pages = len(reader.pages)

    print(f"The PDF document has {num_pages} page(s).")


    # Get the fields in the PDF file

    fields = reader.get_fields()

    print(f"The PDF document has {fields} field(s).")


    # Get the metadata of the PDF file

    # metadata = reader.metadata() # not a function, just a bunch of stuff

    # for key, value in metadata:
        # print(f"{key}: {value}")



    # get the outlines of the PDF file
    # outline = reader.outline()

    # print(f"The PDF document has {len(outline)} outline(s).")



    # # Read text from each page

    for page_num in range(num_pages):

        page = reader.pages[page_num]

        page_text = page.extract_text()
        

        # Print the text from the current page

        print(f"Page {page_num + 1}:\n{page_text}\n")


    # Close the PDF file

    pdf_file.close()



if __name__ == "__main__":
    main()