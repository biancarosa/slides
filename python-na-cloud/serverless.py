from flask import Flask, jsonify

def healthcheck():
    return jsonify({
        "message": "Hello, World!"
    })