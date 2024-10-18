import re
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    sentences = sent_tokenize(text)
    return sentences
