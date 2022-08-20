from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Bad Request</h1>', 300

@app.route('/new/<name>')
def new(name):
    return f'<h1>Hello {name}</h1>'

if __name__ == '__main__':
    app.run(debug=True)