# list are used to store multiple items in single variable.
# list are mutable built in datatype in  python.

num = [2,4,7,8,3,9,6]  # list declaration.
print(num)
print(type(num))
print("length of list",len(num))
print(num[5])
num.remove(4)
print(num)

print(num.pop(0))

num.sort()
print("sorted list is:",num)

num.append(2)
print(num)

num.insert(0,2)
print(num)

# tuple are immutable in  python .



tp = (2,5,8)
print(tp)
