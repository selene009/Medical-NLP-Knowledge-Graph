# src/neo4j_loader.py
"""
Pseudo Neo4j knowledge graph builder.
Does not require a real database — stores triplets internally.
"""

class Neo4jKG:
    def __init__(self):
        # [Originality]
        # This class abstracts the Neo4j graph interface behind a lightweight,
        # in-memory implementation, allowing the NLP pipeline to be demonstrated
        # without external database dependencies.
        #
        # [Result]
        # Enables fast prototyping, easy testing, and clear separation between
        # NLP logic and graph persistence layers.
        self.graph = []
        print("[Init] Pseudo Neo4j Graph created.")

    def add_triplet(self, h, r, t):
        # [Originality]
        # Triplets are stored in (head, relation, tail) form, mirroring
        # Neo4j-style knowledge graph semantics.
        #
        # [Result]
        # Makes the pipeline directly transferable to a real Neo4j backend
        # with minimal code changes.
        self.graph.append((h, r, t))
        print(f"[KG] Added: ({h}) -[{r}]-> ({t})")

    def get_all(self):
        # [Result]
        # Returns all extracted knowledge graph facts for inspection,
        # debugging, or downstream reasoning.
        return self.graph
