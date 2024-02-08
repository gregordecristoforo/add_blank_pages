import PyPDF2

def add_blank_pages(input_pdf_path, output_pdf_path):
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(input_pdf_path)
    
    # Create a PDF writer object
    pdf_writer = PyPDF2.PdfWriter()
    
    # Iterate through all pages in the input PDF
    for page_number in range(len(pdf_reader.pages)):
        # Add the current page to the writer object
        pdf_writer.add_page(pdf_reader.pages[page_number])
        
        # Add a blank page after the current page, unless it's the last page
        if page_number != len(pdf_reader.pages) - 1:
            pdf_writer.add_blank_page()
    
    # Write the modified content to the output PDF file
    with open(output_pdf_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

# Replace 'input.pdf' and 'output.pdf' with the paths to your files
add_blank_pages('input.pdf', 'output.pdf')
