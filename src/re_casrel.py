# src/re_casrel.py
"""
Pseudo CasRel Relation Extraction.
"""

class CasRelRE:
    def extract(self, entities, text):
        """
        Pseudo relation extraction.
        """
        rels = []
        # If both entities appear, create a pseudo "treats" relation
        ents = [e[0] for e in entities]
        if "aspirin" in ents and "headache" in ents:
            rels.append(("aspirin", "treats", "headache"))
        return rels
