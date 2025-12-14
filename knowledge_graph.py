import networkx as nx
import pandas as pd

class KnowledgeGraph:
    def __init__(self):
        """
        Initialize a directed Knowledge Graph
        """
        self.graph = nx.DiGraph()

    def add_relationship(self, entity1, relationship, entity2):
        """
        Add an entity-relationship-entity triple to the graph
        """
        self.graph.add_node(entity1)
        self.graph.add_node(entity2)
        self.graph.add_edge(entity1, entity2, relationship=relationship)

    def add_from_csv(self, csv_path):
        """
        Bulk insert relationships from a CSV file
        CSV format: Entity1,Relationship,Entity2
        """
        df = pd.read_csv(csv_path)

        for _, row in df.iterrows():
            self.add_relationship(
                row["Entity1"],
                row["Relationship"],
                row["Entity2"]
            )

    def query_entity(self, entity):
        """
        Query all outgoing relationships for a given entity
        """
        if entity not in self.graph:
            return []

        results = []
        for neighbor in self.graph.successors(entity):
            results.append({
                "Entity1": entity,
                "Relationship": self.graph[entity][neighbor]["relationship"],
                "Entity2": neighbor
            })
        return results

    def get_all_relationships(self):
        """
        Return all relationships in the knowledge graph
        """
        relationships = []
        for u, v, data in self.graph.edges(data=True):
            relationships.append({
                "Entity1": u,
                "Relationship": data["relationship"],
                "Entity2": v
            })
        return relationships
    
    def get_graph_data(self):
        """
        Return graph data in node-edge format for visualization
        """
        return {
            "nodes": [{"id": n} for n in self.graph.nodes()],
            "edges": [
                {
                    "source": u,
                    "target": v,
                    "label": d["relationship"]
                }
                for u, v, d in self.graph.edges(data=True)
            ]
        }
