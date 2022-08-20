from flask import Flask, make_response, redirect, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def new(name):
    return render_template('user.html', name = name)

if __name__ == '__main__':
    app.run(debug=True)