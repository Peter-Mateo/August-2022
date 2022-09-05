from users_cr_app.config.mysqlconnection import connectToMySQL

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