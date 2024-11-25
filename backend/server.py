from flask import Flask, request, jsonify
from flask_cors import CORS
from bekus_fp_language import run_bekus_fp 
from pymongo import MongoClient

app = Flask(__name__)
CORS(app) 

# MongoDB connection setup
client = MongoClient('mongodb://localhost:27017/')
db = client['bekus_fp_language'] 
collection = db['bekus_fp_language']

@app.route('/api/input', methods=['POST'])
def receive_input():
    try:
        # Get JSON data from request
        data = request.get_json()
        user_input = data.get('userInput')

        if not user_input:
            return jsonify({'error': 'userInput is required'}), 400

        # Check if the value exists in MongoDB
        existing_record = collection.find_one({'userInput': user_input})

        # if existing_record:
        #     output = existing_record.get('output', 'No output found')
        #     print(f"Found in database: {existing_record}")
        # else:
        output = run_bekus_fp(user_input)
            # print(f"Generated output: {output}")

            # collection.insert_one({'userInput': user_input, 'output': output})
            # print("Stored in database.")

        print(f"Received input: {user_input}")
        print(f"Output: {output}")

        return jsonify({'output': output}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Error: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    app.run(port=3001
            
            )  # Run the server on port 3001
