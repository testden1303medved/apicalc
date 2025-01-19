from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/center', methods=['POST'])
def create_user():
    character = request.json.get('x')
    amount = request.json.get('y')
    
    if not character or not isinstance(character, str):
        return jsonify({"error": "Invalid or missing 'x'"}), 400
    if not amount or not isinstance(amount, int):
        return jsonify({"error": "Invalid or missing 'y'"}), 400
    
    x = character * amount
    
    return jsonify({"result": x}), 200

app.run(host='0.0.0.0', port=8080)
