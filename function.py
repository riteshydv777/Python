# sum of two number using function.

# def function1(a,b):
#    sum = a + b
#    return sum
#    print(sum)
#
#
# num1 = int(input("enter number a :"))
# num2 = int(input("enter number b :"))
# s =  function1(num1,num2)
# print(s)

def average(a,b):
    """ This function is used to calculate avarege of two number """
    avg = (a + b)/2
    return avg
num1 = int(input("enter number 1 :"))
num2 = int(input("enter number 2 :"))
# variable to store function return value.

avg = average(num1,num2)
print("average of two number is : ",avg)

print(average.__doc__)  # --doc-- it is documentation string
                        # --doc-- gives coder a brief knowledge about function.
