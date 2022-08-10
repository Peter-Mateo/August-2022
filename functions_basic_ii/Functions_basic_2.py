# Create a list that 
def countdown(x):
    list = []
    for i in range (x):
        list.append(x)
        x = x - 1 
    return list
print(countdown(5))