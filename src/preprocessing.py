# src/preprocessing.py
"""
Basic text preprocessing module (pseudo implementation)
"""

def clean_text(text):
    text = text.lower().strip()
    text = text.replace("\n", " ")
    return text
