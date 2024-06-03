""" ....map() function
"""

items = [1,2,3,4,5,5]
a = list(map((lambda x:x*3),items))
print(a)

""" .....filter() function
"""
a = [1,2,3,4,5,6,7,8]
b = [2,5,8,4,5,6]
c = list(filter(lambda x: x in a , b))
print(c)

""" .....reduce() function 
"""

from functools import reduce

red = reduce(lambda x,y : x*y,[1,2,3,4])
print(red)