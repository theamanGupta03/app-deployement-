from flask import Flask, jsonify, request

app = Flask(__name__)

# Example GET endpoint
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello from Dockerized Flask API!'})

# Example POST endpoint
@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify({'you_sent': data})

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

