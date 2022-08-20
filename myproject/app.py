from flask import Flask, render_template
app = Flask(__name__)

# View function
@app.route('/')
def index():
    return render_template('index.html')

# View function
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
    return render_template('hello.html', name="Peter")

# View function
@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

