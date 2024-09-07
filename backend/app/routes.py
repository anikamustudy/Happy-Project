from app import app
from flask import request, jsonify


@app.route("/")
def home():
    return "Hello Anika!"


@app.route("/api/login", methods=[POST])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if email == "epis08@gmail.com" and password == "ShivaLing@123":
        return jsonify({"success": True})
    else:
        return (jsonify({"success": false, "message": "Invalid credentials"}),)
