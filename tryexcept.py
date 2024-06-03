print("enter num1 : ")
num1 = input()
print("enter num2 : ")
num2 = input()

try:
    # if this line is wrong than our code not crash.
    print("sum of two number is : ", int(num1) + int(num2))
except Exception as e :
    print(e)


print("hello")
