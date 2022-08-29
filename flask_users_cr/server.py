from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL
app = Flask(__name__)

db = 'users_schema'

class User(object):
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW())"
        return connectToMySQL(db).query_db(query,data)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        return connectToMySQL(db).query_db(query,None)


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


if __name__ == '__main__':
    app.run(debug=True)