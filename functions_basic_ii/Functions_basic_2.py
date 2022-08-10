# Create a function that takes input and returns a list counting down from 1 
def countdown(x):
    list = []
    for i in range (x):
        list.append(x)
        x = x - 1 
    return list
print(countdown(5))

#Create a function that takes a list and returns the sum of the first value in the list plus the list's length
def sum(some_list):
    a = some_list[0] + len(some_list)
    return a
