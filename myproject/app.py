from flask import Flask, url_for
app = Flask(__name__)

# View function
@app.route('/')
def index():
    return 'index'

# View function
@app.route('/login')
def login():
    return 'login'

# View function
@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

