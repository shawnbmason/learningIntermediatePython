def painting(paint_colors, picture):
  painting_statement = "To paint the " + picture + " we need the following colors: "
  
#   this would in the local scope
  print(painting_statement)
  
  for color in paint_colors:
      print(color)



painting(['Orange', 'White', 'Green'], 'Indian Flag')