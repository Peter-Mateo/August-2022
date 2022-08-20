from flask import Flask, make_response
app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/new/<name>')
def new(name):
    return f'<h1>Hello {name}</h1>'

if __name__ == '__main__':
    app.run(debug=True)