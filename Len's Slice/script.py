#Declaring list of toppings
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']


#Declaring list of pizza slice costs
prices = [2, 6, 1, 3, 2, 7, 2]

#Your Boss wants you to do some research on $2 slices - Count the number of slices that cost $2 
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

#Find the length of the toppings list 
num_pizzas = len(toppings)

#5
print(f"We sell {num_pizzas} different kinds of pizza!")

#6 
pizza_and_prices = [[2, 'pepperoni'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']]

#8
pizza_and_prices.sort()

#9
cheapest_pizza = pizza_and_prices

#10
priciest_pizza = pizza_and_prices[-1]

#11
pizza_and_prices.pop()

#12
pizza_and_prices.insert(4, [2.5, 'peppers'])

#13
three_cheapest = pizza_and_prices[:3]

#14
print(three_cheapest)