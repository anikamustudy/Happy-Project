from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


# Create the database and the table
with app.app_context():
    db.create_all()

    # Check if the default user already exists
    if not User.query.filter_by(email="test@example.com").first():
        # If not, create the default user
        default_user = User(
            email="test@example.com", password=generate_password_hash("testpassword")
        )
        db.session.add(default_user)
        db.session.commit()


@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"success": False, "message": "No data provided"}), 400

    email = data.get("email")
    password = data.get("password")

    # Query the database for the user
    user = User.query.filter_by(email=email).first()

    # Verify password using hash check
    if user and check_password_hash(user.password, password):
        return jsonify({"success": True, "message": "Login successful"})
    else:
        return jsonify({"success": False, "message": "Invalid credentials"}), 401


if __name__ == "__main__":
    app.run(debug=True)
