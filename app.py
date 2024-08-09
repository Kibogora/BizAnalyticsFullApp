from application import create_app
from flask import render_template, request, redirect, url_for, jsonify

app = create_app()

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/register_users', methods=['POST', 'GET'])
def register_users():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        role = request.form['role']
        password = request.form['password']

        try:
            from application.models.users import User
            User.register_user(email, name, role, password)
            print("User registered successfully!")
            return redirect(url_for('register_users'))
        except Exception as e:
            print("Error registering user:", str(e))
            return jsonify({'error': 'Failed to register user'})
    return render_template('register_users.html')

if __name__ == '__main__':
    app.run(debug=True, port=9000)
