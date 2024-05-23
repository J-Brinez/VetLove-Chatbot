from flask import Flask, request, jsonify
from query_data import query_rag
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Agrega CORS a tu aplicación Flask para permitir solicitudes desde cualquier origen

@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    query_text = data.get('query_text', None)
    if query_text:
        response_text = query_rag(query_text)
        return jsonify({'response': response_text}), 200
    else:
        return jsonify({'error': 'No query text provided'}), 400

if __name__ == '__main__':
    app.run(port=8000, debug=True)
