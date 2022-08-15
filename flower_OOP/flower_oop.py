class Flower:
    def __init__(self, color, type):
        self.color = color
        self.type = type
        self.been_picked = False
        self.height = 1
        self.num_petals = 0

    def grow(self):
        self.height += 3 
        self.num_petals += 2
        return self

    def custom_grow(self, height, num_petals):
        if height or num_petals < 0:
            self.height += height
            self.num_petals += num_petals
            return self
        else:
            print("No negative values")
            return self

    def picked(self):
        self.been_picked = True
        return self

    def planted(self):
        self.been_picked = False 
        return self

    def stepped_on(self):
        new = self.height - 2
        if new < 1:
            return False
        else:
            self.height -= 2
            return self

    def plucked(self):
        pedals = self.num_petals - 1
        if pedals < 0:
            return False
        else:
            self.num_petals -= 1
            return self

    def say_info(self):
        if self.been_picked == True:
            print(" Can't find flower")
            return self
        else:
            print(self.color, self.type, self.been_picked, self.height, self.num_petals)
            return self

# Test

# Declaring the flower
rose = Flower('Red', 'rose')
# Adding Height 
rose.grow().say_info()
print("-" * 15)
# Adding Custom Height
rose.custom_grow(5, 2).say_info()
print("-" * 15)
# Make picked True
rose.picked().say_info()
print("-" * 15)
# Make picked False
rose.planted().say_info()
print("-" * 15)
# Someone accidentally stepped on the rose
rose.stepped_on().say_info()
print("-" * 15)
# We had to pluck dead pedals
rose.plucked().say_info()
print("-" * 15)
