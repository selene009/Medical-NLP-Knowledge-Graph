# src/neo4j_loader.py
"""
Pseudo Neo4j knowledge graph builder.
Does not require a real database — stores triplets internally.
"""

class Neo4jKG:
    def __init__(self):
        self.graph = []
        print("[Init] Pseudo Neo4j Graph created.")

    def add_triplet(self, h, r, t):
        self.graph.append((h, r, t))
        print(f"[KG] Added: ({h}) -[{r}]-> ({t})")

    def get_all(self):
        return self.graph
