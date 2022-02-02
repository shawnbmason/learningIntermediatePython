# paint_gallons_available outside of a function would be a Global Scope
paint_gallons_available = {
    'red': 50,
    'blue': 72,
    'green': 99,
    'yellow': 33
}

def print_available(color):
 
  print('There are ' + str(paint_gallons_available[color]) + ' gallons available of ' + color + ' paint.')


def print_all_colors_available():
    for color in paint_gallons_available:
        print(color)

print_available('red')
print_all_colors_available()


# Giving a variable name a glodal scope namespace
def print_available(color):
    
# global scope namespace
  global paint_gallons_available
  
  paint_gallons_available = {
    'red': 50,
    'blue': 72,
    'green': 99,
    'yellow': 33
  }
  print('There are ' + str(paint_gallons_available[color]) + ' gallons available of ' + color + ' paint.')


print_available('red')
for color in paint_gallons_available:
  print(color)