# src/ner_bert_crf.py
"""
Pseudo BERT + CRF NER model.
Simulates clinical-style NER (e.g., DRUG, DISEASE, SYMPTOM).
"""

class NERModel:
    def __init__(self, model_name="bert-crf-medical"):
        self.model_name = model_name
        print(f"[Init] Loaded pseudo NER model ({model_name})")

    def predict(self, text):
        """
        Pseudo NER output for demonstration.
        Returns list of (entity, label)
        """
        if "aspirin" in text.lower():
            return [("aspirin", "DRUG")]
        if "headache" in text.lower():
            return [("headache", "SYMPTOM")]
        return []
