from app import app
from myproject_app.models.user import User
from flask import render_template

@app.route('/')
def index():
        
    name = User.get_name()
    return render_template('index.html', name = name)