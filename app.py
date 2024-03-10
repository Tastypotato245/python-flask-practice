from flask import Flask, request, jsonify

app = Flask(__name__)

# default is GET methods
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/send', methods=['POST'])
def receive_data():
    data = request.get_json()
    value = data.get('value', None)

    if value is not None:
        return jsonify({"message": "Received", "value": value}), 200
    else:
        return jsonify({"error": "Missing 'value'"}), 400

@app.route('/get_data', methods=['GET'])
def get_data():
    name = request.args.get('name', 'Guest')
    response_data = {
        "message": f"Hello, {name}!",
        "info": "This is a response to a GET request."
    }
    
    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

