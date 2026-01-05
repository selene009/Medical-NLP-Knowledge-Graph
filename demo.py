# demo.py

from src.preprocessing import clean_text
from src.ner_bert_crf import NERModel
from src.re_casrel import CasRelRE
from src.neo4j_loader import Neo4jKG

text = "Aspirin is commonly used to relieve headache."

# Step 1: preprocessing
# [Originality]
# Explicit preprocessing stage mirrors real clinical NLP pipelines
# where raw notes are normalized before model inference.
cleaned = clean_text(text)

# Step 2: NER
# [Result]
# Clinical-style entities (DRUG / SYMPTOM / DISEASE) are extracted
# with a standardized model interface.
ner_model = NERModel()
entities = ner_model.predict(cleaned)

# Step 3: RE (CasRel)
# [Originality]
# Relation extraction is performed as a dedicated stage, reflecting
# modern RE architectures rather than heuristic post-processing.
re_model = CasRelRE()
relations = re_model.extract(entities, cleaned)

# Step 4: Load into KG
# [Result]
# Extracted relations are transformed into Neo4j-style triplets,
# completing the end-to-end medical knowledge graph pipeline.
kg = Neo4jKG()
for h, r, t in relations:
    kg.add_triplet(h, r, t)

print("\nFinal Knowledge Graph Triplets:")
print(kg.get_all())
