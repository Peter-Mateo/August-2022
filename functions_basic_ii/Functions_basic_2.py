# Create a function that takes input and returns a list counting down from 1 
from typing import List


def countdown(x):
    list = []
    for i in range (a):
        list.append(x)
        x = x - 1 
    return list
print(countdown(5))

#Create a function that takes a list and returns the sum of the first value in the list plus the list's length
def sum(some_list):
    print(some_list[0])
    return some_list[1]
num = [1,2]
print(sum(num))

#Create a function that accepts a list and returns the sum of the first value in the list plus the list's length
def summer(some_list):
    a = some_list[0] + len(some_list)
    return a
list = [1,2,3,4,5,6]
print(summer(list))

# Write a function that accpets a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return false. 
def minus(some_list):
    listy = []
    for i in range (len(some_list)):
        if some_list[1] < some_list[i]:
            listy.append(some_list[i])
    print(len(listy))
    if len(listy) < 2:
        return False
    else: 
        return listy 

tapa = [1,2,3,4,5,6,10,1,3,2,1]
false_test = [1,2]
print(minus(tapa))
print(minus(false_test))

# Write a function that that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value. 
def two(size, value):
    list = []
    for i in range(size):
        list.append(value)
    return list
print(two(3,5))