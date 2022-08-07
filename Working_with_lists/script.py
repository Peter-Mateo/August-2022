inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

# Saving How many items in the warehouse to a variable
inventory_len = len(inventory)

#Select the first element in the inventory
first = inventory[0]

#Select the last element from inventory
last = inventory[-1]

#Select items from inventory starting at index 2 and up to but not including, index 6 
inventory_2_6 = inventory[2:6]

#Select the first 3 items of inventory
first_3 = inventory[:3]

#How many 'twin bed' in inventory 
twin_beds = inventory.count("twin bed")

#Remove the 5th element from inventory
removed_item = inventory.pop(4)

#Add "19th Century Bed Frame" in the 11th element in inventory
inventory.insert(10, "19th Century Bed Frame")

#Sort inventory
inventory.sort()
print(inventory)
