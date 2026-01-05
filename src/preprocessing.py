# src/preprocessing.py
"""
Basic text preprocessing module (pseudo implementation)
"""

def clean_text(text):
    # [Originality]
    # Preprocessing is isolated into its own module to reflect real
    # clinical NLP pipelines, where text normalization is decoupled
    # from model inference.
    #
    # [Result]
    # Improves maintainability and ensures consistent text handling
    # across NER and relation extraction stages.
    text = text.lower().strip()
    text = text.replace("\n", " ")
    return text
