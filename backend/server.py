from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Endpoint to receive input data
@app.route('/api/input', methods=['POST'])
def receive_input():
    data = request.get_json()  # Get the JSON data from the request
    user_input = data.get('userInput')
    print(f"Received input: {user_input}")
    
    # Here you can process the input (e.g., save it, transform it, etc.)
    
    return jsonify({'message': 'Input received successfully', 'receivedInput': user_input}), 200

if __name__ == '__main__':
    app.run(port=3001)  # Run the server on port 3001
