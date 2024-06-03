#
# import tut1
# print("__name__ in tut2.py is set to " , __name__)

def printhar(String):
    return f" programmer is {String}"
def add(num1 , num2):
    return num1 + num2 + 5

print("name is " , __name__)

if __name__ == '__main__' :
    print(printhar("harry7"))
    o = add(4,6)
    print(o)