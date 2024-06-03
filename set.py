# set in python is data type uniquely define.

s = set()
print(type(s))

l = [1,2,3,4,5]
s1 = set(l)
print(s1)

s.add(1)
s.add(2)
print(s)

s.remove(2)

print(s)

s1 = {4,6}
print(s.union(s1))

