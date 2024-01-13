from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A dictionary to store user credentials (in a real application, use a database)
users = {
    'user1': 'password1',
    'user2': 'password2',
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return f'Welcome, {username}!'
    else:
        return 'Login failed. Please check your username and password.'

if __name__ == '__main__':
    app.run(debug=True)
