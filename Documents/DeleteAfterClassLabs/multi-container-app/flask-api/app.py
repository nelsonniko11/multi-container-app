from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app

@app.route('/api/generate', methods=['POST'])
def generate_text():
    data = request.get_json()
    query = data['query']
   
    # Simulate interaction with Databricks Dolly for text generation
    generated_text = f"Dolly's response to '{query}'"
    return jsonify({'generated_text': generated_text})
   
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)