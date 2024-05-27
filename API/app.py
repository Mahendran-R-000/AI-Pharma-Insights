from flask import Flask, request, jsonify
import pickle
import os

# Get the current working directory
cwd = os.getcwd()

# Specify the path to the dataset file
path = os.path.join(cwd, 'Model/data.pkl')

# Load the cleaned data
with open(path, 'rb') as f:
    drug_data_cleaned = pickle.load(f)

app = Flask(__name__)

@app.route('/drug_info', methods=['GET'])
def get_drug_info():
    condition = request.args.get('condition')
    if not condition:
        return jsonify({"error": "Condition not provided"}), 400

    filtered_data = drug_data_cleaned[drug_data_cleaned['condition'].str.lower()== condition.lower()]
    if filtered_data.empty:
        return jsonify({"error": "No data found for the provided condition"}), 404
    sorted_data = filtered_data.sort_values(by='usefulness_score', ascending=False)
    result = sorted_data[['drugName', 'usefulness_score']].to_dict(orient='records')
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True,host="127.0.0.1",port=5000)
