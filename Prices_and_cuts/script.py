hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
# Create variable for sum of all the prices
total_price = 0
# Creates a loop to iterate over prices and add them to total_price
for price in prices:
    total_price += price
# Creates the average price
average_price = total_price / len(prices)
# Print the values
print(f"Average Haircut Price: {average_price}")
# Creates a list comprehension to lower the prices 
new_prices = [price - 5 for price in prices]
# Prints list comprehension to lower the prices
print(new_prices)
# Declaring variable
total_revenue = 0
# Find total revenue
for i in range(len(hairstyles)):
    total_revenue += prices[i] + last_week[i]
# Print total_revenue
print(f"Total Revenue: {total_revenue}")
# Find the daily average
average_daily_revenue = total_revenue / 7
# Print daily average
print(average_daily_revenue)
# Creates a variable with just the haircuts that cost 30 and below
cuts_under_30 = [hairstyles[i] for i in range(len(prices)-1) if prices[i] <= 30]
# Print Cuts
print(cuts_under_30)