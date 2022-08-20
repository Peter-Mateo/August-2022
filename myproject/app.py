from flask import Flask, url_for
app = Flask(__name__)

# View function
@app.route('/')
def index():
    return 'Index page'

# View function
@app.route('/login/')
def hello():
    return 'login'

# View function
@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next = '/'))
    print(url_for('profile', next = '/'))
