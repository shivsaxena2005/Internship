from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = 'task_4.json'


def load_file():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)


def save_file(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)


# ---------- GET ----------
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    data = load_file()
    if user_id in data:
        return jsonify({user_id: data[user_id]}), 200
    else:
        return jsonify({"error": "User not found"}), 404


# ---------- POST ----------
@app.route('/users', methods=['POST'])
def create_user():
    new_data = request.get_json()
    if not new_data or len(new_data) != 1:
        return jsonify({"error": "Send exactly one user as JSON"}), 400

    data = load_file()
    key = list(new_data.keys())[0]
    if key in data:
        return jsonify({"error": "User already exists"}), 400

    data[key] = new_data[key]
    save_file(data)
    return jsonify({"message": "User added successfully"}), 201


# ---------- PUT ----------
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    updated_data = request.get_json()
    if not updated_data or len(updated_data) != 1:
        return jsonify({"error": "Send exactly one user as JSON"}), 400

    data = load_file()
    if user_id not in data:
        return jsonify({"error": "User not found"}), 404

    # Delete old entry and insert new data
    del data[user_id]
    new_key = list(updated_data.keys())[0]
    data[new_key] = updated_data[new_key]
    save_file(data)
    return jsonify({"message": "User updated successfully"}), 200


# ---------- DELETE ----------
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    data = load_file()
    if user_id not in data:
        return jsonify({"error": "User not found"}), 404

    del data[user_id]
    save_file(data)
    return jsonify({"message": "User deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)
