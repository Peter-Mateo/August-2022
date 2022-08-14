class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member=False, gold_card_points = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points

    def display_info(self):
        print(
        "\n", self.first_name, 
        "\n", self.last_name, 
        "\n", self.email, 
        "\n", self.age, 
        "\n", self.is_rewards_member, 
        "\n", self.gold_card_points)

    def enroll(self):
        if self.is_rewards_member == True:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True
        else:
            print("User already a member")
            return False

    def spend_points(self,amount):
        if self.gold_card_points < amount:
            print("Not enough Funds")
        else:
            self.gold_card_points -= self.gold_card_points - amount

## Test ###
student = User('Peter', 'Mateo', 'asp@gmail.com', 21)

student.enroll()
student.spend_points(100)
student.display_info()
student.enroll()
student.spend_points(400)