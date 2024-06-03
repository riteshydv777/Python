def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac
num = int(input("enter number"))
print("factorial using iterative is : ",factorial_iterative(num))

# factorial using recursion

def fact_recursion(n):
    if n == 1:
        return 1
    else:
        return n * fact_recursion(n-1)

num1 = int(input("enter number:"))
print("factorial using recursion is :", fact_recursion(num1))

