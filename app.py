from flask import Flask, render_template, request, jsonify
from knowledge_graph import KnowledgeGraph
import os

app = Flask(__name__)
kg = KnowledgeGraph()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add():
    data = request.json
    kg.add_relationship(
        data["entity1"],
        data["relationship"],
        data["entity2"]
    )
    return jsonify({"status": "success"})

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)
    kg.add_from_csv(path)
    return jsonify({"status": "csv uploaded"})

@app.route("/query")
def query():
    entity = request.args.get("entity")
    return jsonify(kg.query_entity(entity))

@app.route("/graph")
def graph():
    return jsonify(kg.get_graph_data())

if __name__ == "__main__":
    app.run(debug=True)
