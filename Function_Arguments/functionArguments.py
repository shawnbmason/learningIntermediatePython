tables = {
  1: ['Jiho', False],
  2: [],
  3: [],
  4: [],
  5: [],
  6: [],
  7: [],
}
print(tables, "\n")

def assign_table(table_number, name, vip_status = False):
  tables[table_number] = [name, vip_status]
  
assign_table(6, "Yoni", False)
print(tables, "\n")

assign_table(table_number = 3, name = "Martha", vip_status = True)
print(tables, "\n")

assign_table(4, "Karla")
print(tables, "\n")


# Variable number of arguments: *args

# Unpacking operator(*)

# The unpacking operator allows us to 
# give our functions a variable number of 
# arguments by performing what’s known as 
# positional argument packing.
def print_order(*order_item):
  print(order_item)
  
print_order('Orange Juice', 'Apple Juice', 'Scrambled Eggs', 'Pancakes')


# Working with *args
tables = {
  1: {
    'name': 'Jiho',
    'vip_status': False,
    'order': 'Orange Juice, Apple Juice'
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {}
}
print(tables, "\n")

def assign_table(table_number, name, vip_status = False):
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = ''
  
def assign_and_print_order(table_number, *order_items):
  tables[table_number]['order'] = order_items
  for orders in order_items:
    print(orders)
    
assign_table(2, 'Arwa', True)
assign_and_print_order(2, 'Steak', 'Seabass', 'Wine Bottle')

print('\n')
print(tables, '\n')


# Variable number of arguments: **kwargs
tables = {
  1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
print(tables)

def assign_food_items(**order_items):
  print(order_items)
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  print(food)
  print(drinks)
# Example Call
assign_food_items(food='Pancakes, Poached Egg', drinks='Water')


# Working with **kwargs
tables = {
  1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}

def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = {}

assign_table(2, 'Douglas', True)
print('\n--- tables with Douglas --- \n', tables)

def assign_food_items(table_number, **order_items):
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  tables[table_number]['order']['food_items'] = food
  tables[table_number]['order']['drinks'] = drinks

print('\n --- tables after update --- \n')

assign_food_items(2, food = 'Seabass, Gnocchi, Pizza', drinks = 'Margarita, Water')

print(tables, "\n")


# All together now! *args and **kwargs
def single_prix_fix_order(appetizer, *entrees, sides, **dessert_scoops):
  print("Appetizer:", appetizer, "\n")
  print("Entrees:", entrees, "\n")
  print("Sides:", sides, "\n")
  print("Dessert scoops of icecream:", dessert_scoops, "\n")

single_prix_fix_order('Baby Beets', 'Salmon', 'Scallops', 
                      sides = 'Mashed Potatoes', 
                      dessert_scoops1 = 'Vanilla', 
                      dessert_scoops2 = 'Cookies and Cream')


# Function Call Unpacking
def calculate_price_per_person(total, tip, split):
  total_tip = total * (tip/100)
  split_price = (total + total_tip) / split
  print(split_price)

table_7_total = [534.50, 20.0, 5]

calculate_price_per_person(*table_7_total)