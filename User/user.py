
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

    def get_all(self):
        print(
            self.first_name, 
            self.last_name, 
            self.email, 
            self.age
        )
    
    def get_name(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name

student = User('Leo', 'Mateo', 'Leon@gmai.com', 21)
student1 = User('Peter', 'Mateo', 'peter.mateo123@gmail.com', 21)

student.get_all()
print('-'*15)
student1.get_all()
print('-'*15)

