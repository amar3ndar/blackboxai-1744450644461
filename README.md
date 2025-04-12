
Built by https://www.blackbox.ai

---

```markdown
# PDF Inverter

## Project Overview
PDF Inverter is a simple web application built with Flask that allows users to upload PDF files and convert their color scheme to black and white. This tool is particularly useful for making PDFs more printer-friendly or for users who prefer reading in black and white.

## Installation
To set up PDF Inverter on your local machine, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your_username/pdf-inverter.git
   cd pdf-inverter
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   Make sure you have Python 3 and pip installed, and then run:
   ```bash
   pip install Flask PyPDF2
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```
   By default, the application will run on [http://localhost:5005](http://localhost:5005).

## Usage
1. Open your web browser and go to [http://localhost:5005](http://localhost:5005).
2. Use the file input to upload a PDF document.
3. Click the "Upload PDF" button.
4. The application will process the PDF and download the inverted version automatically.

## Features
- Upload PDF files and convert them to black and white.
- Simple and user-friendly interface.
- Responsive design using Tailwind CSS.

## Dependencies
This project depends on the following Python packages, which will be installed when you run the installation steps:
- `Flask`: A lightweight WSGI web application framework.
- `PyPDF2`: A library for manipulating PDF files in Python.

If using `pip`, you can include them in `requirements.txt` like this:
```
Flask==2.0.1
PyPDF2==1.26.0
```

## Project Structure
```
pdf-inverter/
│
├── app.py            # Main application file with backend logic
├── index.html        # Frontend HTML file
├── style.css         # Optional styles for the application
└── requirements.txt   # List of dependencies (if created)
```

## Acknowledgements
- [Flask Documentation](https://flask.palletsprojects.com/)
- [PyPDF2 Documentation](https://pypdf2.readthedocs.io/)
- [Tailwind CSS](https://tailwindcss.com/)
```