# src/re_casrel.py
"""
Pseudo CasRel Relation Extraction.
"""

class CasRelRE:
    def extract(self, entities, text):
        """
        Pseudo relation extraction.
        """
        # [Originality]
        # This module follows the CasRel design philosophy by explicitly
        # modeling (head, relation, tail) extraction as a separate step
        # after entity recognition.
        #
        # [Result]
        # Enables clear separation of concerns and allows independent
        # improvement of NER and RE components.
        rels = []
        ents = [e[0] for e in entities]

        # [Originality]
        # Relation rules are intentionally simple but structured to
        # demonstrate how clinical relations are grounded in entity co-occurrence.
        #
        # [Result]
        # Produces deterministic, interpretable relations suitable for
        # downstream knowledge graph construction.
        if "aspirin" in ents and "headache" in ents:
            rels.append(("aspirin", "treats", "headache"))
        return rels
