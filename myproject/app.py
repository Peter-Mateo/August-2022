from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)

# View function
@app.route('/')
def index():
    return redirect(url_for('login'))

# View function
@app.route('/login')
def login(name = None):
    return render_template('hello.html', name= 'Peter')

# View function
@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

