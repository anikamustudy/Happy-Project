from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS

app = Flask(_name_)
CORS(app)

#Configuring the SQLite database
app.config['SQLALCHEMY_DATABASE'] = 'sqlite://users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db= SQLAlchemy(app)
bcrypt = Bcrypt(app)

#User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Sting(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password =db.Column(db.String(200), nullable=False)
    
    #Create the database
    with app.app_context():
        db.create_all()
        
    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        username = data['username']
        email = data['email']
        password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        
        #Check if user already exists
        
        existing_user = User.query.filter((User.username == username) | (User.email  == email))    
        
        if existing_user:
            
            return jsonify({'message':'User already exists'}), 409
        
        #Create a new user
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({'message': 'User registered successfully!'}), 201
    if __name__== '_main_':
        app.run(debug=True)
        
        