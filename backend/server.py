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
        if isinstance(output, list):
            output = (str(output).replace('[', '(').replace(']', ')')).replace(',', '').replace('\'', '')
            output = output.replace('True', 'true').replace('False', 'false').replace('None', 'nil').replace('Nil', 'nil')
        
            # print(f"Generated output: {output}")

            # collection.insert_one({'userInput': user_input, 'output': output})
            # print("Stored in database.")

        # print(f"Received input: {user_input}")
        # print(f"Output: {output}")

        output = str(output)
        output = output.replace('True', 'true').replace('False', 'false').replace('None', 'nil').replace('Nil', 'nil')

        return jsonify({'output': output}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Error: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    app.run(port=5000
            
            )  # Run the server on port 5000
