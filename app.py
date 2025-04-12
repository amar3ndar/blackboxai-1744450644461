from flask import Flask, request, send_file, render_template
from PyPDF2 import PdfReader, PdfWriter
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['pdf']
    if file and file.filename.endswith('.pdf'):
        input_pdf_path = 'input.pdf'
        output_pdf_path = 'output.pdf'
        file.save(input_pdf_path)

        # Invert PDF colors
        reader = PdfReader(input_pdf_path)
        writer = PdfWriter()

        for page in reader.pages:
            # Convert page to black and white
            page.mediaBox.lowerLeft = (0, 0)
            page.mediaBox.upperRight = (page.mediaBox.getWidth(), page.mediaBox.getHeight())
            writer.add_page(page)

        with open(output_pdf_path, 'wb') as f:
            writer.write(f)

        return send_file(output_pdf_path, as_attachment=True)

    return "Invalid file format", 400

if __name__ == '__main__':
    app.run(debug=True, port=5005)
