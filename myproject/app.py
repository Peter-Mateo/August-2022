from flask import Flask
app = Flask(__name__)

# View function
@app.route('/')
def index():
    return 'Index page'

# View function
@app.route('/hello')
def hello():
    return 'Hello, World'