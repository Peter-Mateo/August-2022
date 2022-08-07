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

for x in range(5): # for - Start 
    print(x)
#Stop
for x in range(2,5): # for - Start
    print(x)
#Stop
for x in range(2,10,3): # for - Increment by 3 
    print(x)
#Stop
x = 0 # Variable declaration
while(x < 5): # while - Start
    print(x)
    x += 1
#Stop

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)