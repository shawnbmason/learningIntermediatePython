letters = ['r', 'e', 'd', 'u', 'c', 'e']

# remember to import the reduce function
from functools import reduce
# store the result of your reduce function in the variable word
word = reduce(lambda x,y: x+y, letters)

# print word
print(word)


# another example
from functools import reduce
 
int_list = [3, 6, 9, 12]
 
reduced_int_list = reduce(lambda x,y: x*y, int_list)
 
print(reduced_int_list)