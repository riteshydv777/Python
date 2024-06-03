# def function():
#     print("hello ")
# function()
#
# func2 = function
# del function
# func2()
#
# def funcreturn(num):
#     if num == 0 :
#         return print
#     if num == 1 :
#         return sum
#
# a = funcreturn(1)
# print(a)
#
# def executor(func):
#     func("this")
#
# executor(print)

""" ..... Decorators in Python......
"""

def dec1(func1):
    def nowexec():
        print("Executing Now")
        func1()
        print("Executed")
    return nowexec
# @dec1
def name():
    print("I am Ritesh")

name = dec1(name)
name()