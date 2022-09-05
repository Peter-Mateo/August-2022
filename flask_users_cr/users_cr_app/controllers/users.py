from users_cr_app import app
from flask import  render_template, redirect, request
from users_cr_app.models import User



@app.route('/users')
def index():
    users = User.get_all()
    print(users)
    return render_template('users.html', users = users)

@app.route('/users/new')
def new():
    return render_template('new.html')

@app.route('/users/processed', methods=['POST'])
def processed():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'], 
        "email": request.form['email']
    }
    User.save(data)
    return redirect('/users')