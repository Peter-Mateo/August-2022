class flower:
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

    def custom_grow(self, hieght, num_petals):
        if hieght or num_petals < 0:
            print("No negative values")
            return self
        else:
            self.height = hieght
            self.num_petals = num_petals
            return self

    def picked(self):
        self.been_picked = True
        return self

    def planted(self):
        self.been_picked = False 
        return self

    def stepped_on(self):
        if (self.height -= 2) < 0:
            return False
        else:
            self.height -= 2
            return self

