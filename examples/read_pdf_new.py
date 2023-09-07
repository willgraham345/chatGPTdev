import pdfplumber as pdfp

pdf = pdfp.open('examples/convolutional_neural_networks.pdf')

print("Extracting words")
with open('convolutional_neural_networks_words.txt', 'w') as f:
    for page in pdf.pages:
        words = page.extract_words(use_text_flow=True, keep_blank_chars=True, )
        for w in words:
            # print(w['text'])
            f.write(str(w['text']))
        # print('----------------------')
    f.close()
    # Best method for sure. Use this to extract text from pdfs.

print("=====================================")

print("Extracting text")
with open('convolutional_neural_networks_text.txt', 'w') as f:
    for page in pdf.pages:
        text = page.extract_text()
        # print(text) 
        f.write(str(text))
        # print('----------------------')
    f.close() 

print("=====================================")

print("Extractinig Text Lines")
with open('convolutional_neural_networks_text_lines.txt', 'w') as f:
    for page in pdf.pages:
        text_lines = page.extract_text(x_tolerance=2, y_tolerance=0)
        # print(text_lines)
        f.write(str(text_lines))
        # print('----------------------')
    f.close()