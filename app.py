from flask import Flask, render_template, request, jsonify
import json
import numpy as np
import google.generativeai as genai

# ADD YOUR API KEY HERE
import os
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

# Load documents
with open("docs.json") as f:
    documents = json.load(f)

# Generate embeddings
def generate_embedding(text):
    result = genai.embed_content(
        model="models/gemini-embedding-001",
        content=text
    )
    return np.array(result["embedding"])

# Store embeddings
doc_embeddings = []

for doc in documents:
    emb = generate_embedding(doc["content"])
    doc_embeddings.append((doc["content"], emb))

# Cosine similarity
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Retrieve relevant docs
def retrieve_docs(query):
    query_emb = generate_embedding(query)

    scores = []
    for doc, emb in doc_embeddings:
        score = cosine_similarity(query_emb, emb)
        scores.append((doc, score))

    scores.sort(key=lambda x: x[1], reverse=True)

    return [s[0] for s in scores[:3]]

# Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

    context_docs = retrieve_docs(user_message)

    context = "\n".join(context_docs)

    prompt = f"""
Use the following context to answer the question.

Context:
{context}

User: {user_message}
Assistant:
"""

    response = model.generate_content(prompt)

    return jsonify({"reply": response.text})


if __name__ == "__main__":
    app.run(debug=True)