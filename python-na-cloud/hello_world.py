from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world(req):
    return jsonify({
        "message": "Hello, World!"
    })

