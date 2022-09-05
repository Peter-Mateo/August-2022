from flask import Flask
from recipes_app.controllers import users


app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)