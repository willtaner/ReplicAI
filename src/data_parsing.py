import os
import docx
import PyPDF2

def parse_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def parse_docx(file_path):
    doc = docx.Document(file_path)
    return '\n'.join([para.text for para in doc.paragraphs])

def parse_pdf(file_path):
    text = ''
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def parse_documents(data_dir):

    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    data_dir = os.path.join(root, data_dir)    

    texts = []
    for filename in os.listdir(data_dir):
        file_path = os.path.join(data_dir, filename)
        if filename.endswith('.txt'):
            texts.append(parse_txt(file_path))
        elif filename.endswith('.docx'):
            texts.append(parse_docx(file_path))
        elif filename.endswith('.pdf'):
            texts.append(parse_pdf(file_path))
    return texts