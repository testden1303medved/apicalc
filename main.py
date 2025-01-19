from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/center', methods=['POST'])
def create_user():
    character = request.json.get('x')
    amount = request.json.get('y')
    
    if not character:
        return jsonify({"error": "missing 'x'"}), 400
    if not amount:
        return jsonify({"error": "missing 'y'"}), 400
    
    x = character * int(amount)
    
    return jsonify({"result": x}), 200

app.run(host='0.0.0.0', port=8080)
