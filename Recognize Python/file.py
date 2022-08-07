num1 = 42 # Integer
num2 = 2.3 # Float
boolean = True # Boolean
string = 'Hello World' # String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # List Initialization
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Dictionary initialisation
fruit = ('blueberry', 'strawberry', 'banana') # Tuple initialisation
print(type(fruit)) # Type Check
print(pizza_toppings[1]) # List - Access Value - 'Sausage'
pizza_toppings.append('Mushrooms') # List - Add Value
print(person['name']) # Dictionary - Access Value - 'John'
person['name'] = 'George' # Dictionary - Change Value - 'George'
person['eye_color'] = 'blue' # Dictionary - Add Value - 'eye_color': 'blue'
print(fruit[2]) # Tuple - Access Value - 'banana'

if num1 > 45: # if 
    print("It's greater")
else: # else
    print("It's lower")

if len(string) < 5: # Length Check
    print("It's a short word!")
elif len(string) > 15: # Length Check
    print("It's a long word!")
else: # else
    print("Just right!")

for x in range(5): # for - Sequence
    # for - Start 
    print(x)
    #for - Increment
#Stop
for x in range(2,5): # for - Sequence
    # for - Start
    print(x)
    # for - Increment
#Stop
for x in range(2,10,3): # for - Sequence
    # for - Start
    print(x)
    # for - Increment by 3 
#Stop
x = 0 # Variable declaration
while(x < 5): # while - Start
    print(x)
    x += 1 # while - Increment
#Stop

pizza_toppings.pop() # List - Delete last Value
pizza_toppings.pop(1) # List - Delete 'Sausage'

print(person) # Dictionary - Access Value 
person.pop('eye_color') # Dictionary - Delete Value 
print(person) # Dictionary - Access Value

for topping in pizza_toppings: # for - Sequence 
    # for - Start
    if topping == 'Pepperoni':
        continue # for - continue 
    print('After 1st if statement')
    if topping == 'Olives':
        break # for - break 
    # for - Increment

def print_hello_ten_times(): # Function
    for num in range(10):
        print('Hello')

print_hello_ten_times() # Function - Call 

def print_hello_x_times(x): # Function - Argument
    for num in range(x):
        print('Hello')

print_hello_x_times(4) # Function - Argument

def print_hello_x_or_ten_times(x = 10): # Function - Parameter 
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() # Function - Call
print_hello_x_or_ten_times(4) # Function - Argument


""" # Multi-Line Comment
Bonus section
"""

# print(num3) # Name ERROR name <num3> is not defined
# num3 = 72 # Variable Declaration
# fruit[0] = 'cranberry' # Type Error: 'tuple' object does not support item assignment 
# print(person['favorite_team']) # KeyError: 'favorite_team'
# print(pizza_toppings[7]) # IndexError: list index out of range 
#   print(boolean) # IndentationError: unexpected indent
# fruit.append('raspberry') # AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) # AttributeError: 'tuple' object has no attribute 'pop'