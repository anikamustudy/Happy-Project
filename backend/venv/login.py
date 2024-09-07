from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy user data for demonstration
users = {
    "test@example.com": "testpassword"
}

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    # Validate the credentials
    if email in users and users[email] == password:
        return jsonify({"success": True, "message": "Login successful"})
    else:
        return jsonify({"success": False, "message": "Invalid credentials"})

if __name__ == '__main__':
    app.run(debug=True)
