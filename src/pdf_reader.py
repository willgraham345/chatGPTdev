import PyPDF2 as pdf2
import nltk

class PDFReader():
    """
    Class to read PDF files and extract text from them

    Parameters: 
    pdf_file: PDF file to be read

    Methods:
    get_num_pages: return the number of pages in the PDF file
    get_fields: return the fields in the PDF file
    get_outline: return the outline of the PDF file
    get_text: return the text from each page of the PDF file
    export_text: export the text from each page of the PDF file to a text file
    
    """
    def __init__(self, pdf_file):
        self.pdf_file = pdf_file
    
    def format_document(self):
        """
        Format the PDF document

        Returns:
        formatted_doc: Formatted JSON file, with the following structure:
        {
            "title": "Title of the paper",
            "authors": [
                {
                    "name": "Name of the author",
                    "affiliation": "Affiliation of the author"
                },
                ...
            ],
            "abstract": "Abstract of the paper",
            "sections": [
                {
                    "title": "Title of the section",
                    "text": "Text of the section"
                },
                ...
            ],
            "references": [
                {
                    "title": "Title of the reference",
                    "authors": [
                        {
                            "name": "Name of the author",
                            "affiliation": "Affiliation of the author"
                        },
                        ...
                    ],
                    "venue": "Venue of the reference",
                    "year": "Year of the reference"
                },
                ...
            ]
        }

        """
        pass




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



    # get the outlines of the PDF file
    outline = reader.outline

    print(f"The PDF document has {len(outline)} outline(s).")



    # # Read text from each page
    full_text = []
    for page_num in range(num_pages):

        page = reader.pages[page_num]

        page_text = page.extract_text()
        full_text.append(page_text)

        # Print the text from the current page
        # print(f"Page {page_num + 1}:\n{page_text}\n")

    # export full_text to a text file
    with open('examples/convolutional_neural_networks.txt', 'w') as file:
        for item in full_text:
            file.write("%s\n" % item)

        # Close file
        file.close()

    
    # Close the PDF file

    pdf_file.close()



if __name__ == "__main__":
    main()