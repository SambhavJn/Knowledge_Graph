from knowledge_graph import KnowledgeGraph

kg = KnowledgeGraph()


kg.add_from_csv("transport_network.csv")
# ---- Manual Input (Transportation Network Example) ----
# kg.add_relationship("Bangalore", "connected_by", "Train")
# kg.add_relationship("Bangalore", "has_airport", "Kempegowda Airport")
# kg.add_relationship("Train", "connects_to", "Chennai")
# kg.add_relationship("Bus", "connects_to", "Mysore")

# ---- Query Example ----
print("Query Results for Bangalore:")
results = kg.query_entity("Bangalore")
for r in results:
    print(r)

# ---- Display Entire Knowledge Graph ----
print("\nAll Relationships in Knowledge Graph:")
for r in kg.get_all_relationships():
    print(r)
