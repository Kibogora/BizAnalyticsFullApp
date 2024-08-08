from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from application.models.users import  User
import logging


app = Flask(__name__)

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/blogapplication'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

# Reflect the existing database or create tables
with app.app_context():
    app.db = db
    db.create_all(bind=db.engine)
    
@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/register_users', methods=['POST', 'GET'])
def register_users():
    if request.method == 'POST':
    
        email = request.form['email']
        print("Email:", email)
        name = request.form['name']
        print("Name:", name)
        role = request.form['role']
        print("role:", role)
        password = request.form['password']
        print("Password:", password)
    
        try:
            result = User.register_user(email, name, role, password)
            print("User registered successfully!")
            return redirect(url_for('register_users'))
        except Exception as e:
            print("Error registering user:", str(e))
            return jsonify({'error': 'Failed to register user'})
    return render_template('register_users.html')
    
if __name__ == '__main__':
    app.run(debug=True, port=9000)
