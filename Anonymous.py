# Inline function

'''''.....lembda expression ... '''''

# result = lambda n1,n2,n3 : n1+n2+n3
# print("sum of numbers is : " , result(10,20,30))

'''    without lembda  '''

'''
def function1(a,b ,c):
    sum = a + b + c
    return sum

n1 = 10
n2 = 20
n3 = 30

s = function1(n1,n2,n3)
print(s)
'''
#
# def add(a,b):
#     return a+b
# print(add(10,20))

add = lambda a,b : a + b
print("sum of number is : ", add(10,20))

minus = lambda x,y : x-y
print("sub of number is : ", minus(7,4))
