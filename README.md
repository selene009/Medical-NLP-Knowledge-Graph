# Medical NLP Knowledge Graph (NER + RE + Neo4j)

A lightweight demonstration of a medical NLP pipeline consisting of:
- Clinical-style NER using a pseudo BERT + CRF model  
- Relation Extraction using a pseudo CasRel module  
- Knowledge Graph construction using a Neo4j-like interface  

This project is designed as a portfolio-friendly representation of a real clinical NER/RE/Neo4j workflow.  
Suitable for medical AI, clinical NLP, and healthcare knowledge graph engineering roles.

---

## Features
- NER model (BERT-CRF style) simulated for DRUG / SYMPTOM / DISEASE
- CasRel-style relation extraction
- Knowledge graph builder with Neo4j-style triplets
- Clinical-like pipeline structure without real PHI data
- Easy to extend to real models (HuggingFace, PyTorch, Neo4j)

## Project Structure
medical-nlp-kg/
src/
preprocessing.py
ner_bert_crf.py
re_casrel.py
neo4j_loader.py
demo.py
requirements.txt
README.md


---

## ▶ Run Demo
python demo.py

Expected output:
[KG] Added: (aspirin) -[treats]-> (headache)

---

## 🔧 Next Steps (if using real models)
- Replace `NERModel` with a HuggingFace + CRF model  
- Replace `CasRelRE` with a trained CasRel model  
- Replace `Neo4jKG` with an actual Neo4j driver  
- Add Doccano annotation workflow  

---






## 📂 Project Structure

