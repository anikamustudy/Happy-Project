from app import db, User

with db.app.app_context():
    # Print all users in the database
    users = User.query.all()
    for user in users:
        print(f"User ID: {user.id}, Email: {user.email}, Password: {user.password}")
