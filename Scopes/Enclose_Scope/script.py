def calc_paint_amount(width, height):

  square_feet = width * height
  # Write your code below!
  def calc_gallons():
      return square_feet / 400
  
# this would be a Enclosing Scope
  return calc_gallons()
  
print('Number of paint gallons needed: ')
print(str(calc_paint_amount(30,20)))



# another example of Nonlocal Scope

walls = [(20, 9), (25, 9), (20, 9), (25, 9)]


def calc_paint_amount(wall_measurements):

  square_feet = 0

  def calc_square_feet():
    
    # this is what a nonlocal looks like
    nonlocal square_feet
    
    for width, height in wall_measurements:
      square_feet += width * height

  def calc_gallons():
    return square_feet / 400

  calc_square_feet()

  return calc_gallons()


print('Number of paint gallons needed: ')
print(str(calc_paint_amount(walls)))