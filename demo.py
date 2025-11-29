# demo.py

from src.preprocessing import clean_text
from src.ner_bert_crf import NERModel
from src.re_casrel import CasRelRE
from src.neo4j_loader import Neo4jKG

text = "Aspirin is commonly used to relieve headache."

# Step 1: preprocessing
cleaned = clean_text(text)

# Step 2: NER
ner_model = NERModel()
entities = ner_model.predict(cleaned)

# Step 3: RE (CasRel)
re_model = CasRelRE()
relations = re_model.extract(entities, cleaned)

# Step 4: Load into KG
kg = Neo4jKG()
for h, r, t in relations:
    kg.add_triplet(h, r, t)

print("\nFinal Knowledge Graph Triplets:")
print(kg.get_all())
