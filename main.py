from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/center', methods=['POST'])
def center_calculator():
    word  = str(request.json.get('x'))
    width = int(request.json.get('y'))
    fill  = str(request.json.get('z'))
    
    if not word : return jsonify({"error": "missing 'x'"}), 400
    if not width: return jsonify({"error": "missing 'y'"}), 400
    if not fill : fill = " "
    
    total_padding = max(0, width - len(word))
    left_padding  = total_padding // 2
    right_padding = total_padding - left_padding
    
    left_fill  = (fill * (left_padding // len(fill) + 1))[:left_padding]
    right_fill = (fill * (right_padding // len(fill) + 1))[:right_padding]

    
    return jsonify({"result": f"{left_fill}$$${right_fill}"}), 200
    
if __name__ == "__main__":
    app.run(port=8080)
