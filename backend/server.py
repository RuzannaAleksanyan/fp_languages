from flask import Flask, request, jsonify
from flask_cors import CORS
from bekus_fp_language import run_bekus_fp 

app = Flask(__name__)
CORS(app) 

@app.route('/api/input', methods=['POST'])
def receive_input():
    data = request.get_json() 
    user_input = data.get('userInput')
    # stugum db-um
    output = run_bekus_fp(user_input)
    # save db
    print(f"Received input: {user_input}")
    
    return jsonify({'message': 'Input received successfully', 'receivedInput': user_input}), 200

if __name__ == '__main__':
    app.run(port=3001)  # Run the server on port 3001
