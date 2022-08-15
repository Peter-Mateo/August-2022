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



