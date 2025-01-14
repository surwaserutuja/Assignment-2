from flask-cors import  CORS,Flask, request, jsonify
import json

app = Flask(__name__)
CORS(app)

# Load documentation
with open("documentation.json") as f:
    documentation = json.load(f)

@app.route('/chat', methods=['POST'])
def chat():
    query = request.json.get("query", "").lower()

    # Basic keyword matching
    for item in documentation:
        if any(keyword in query for keyword in item["keywords"]):
            return jsonify({"answer": item["response"]})

    return jsonify({"answer": "Sorry, I couldn't find an answer to your question."})

if __name__ == '__main__':
    app.run(debug=True)

