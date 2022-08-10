# Create a function that takes input and returns a list counting down from 1 
def countdown(x):
    list = []
    for i in range (x):
        list.append(x)
        x = x - 1 
    return list
print(countdown(5))