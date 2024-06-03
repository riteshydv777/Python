 # enumerate(iterable , start = 0)

list = ["code" , "with" , "harry"]
for index , value in enumerate(list, 1):
    print(index , value)
#
# list1 = ["Tony","jack","john","harry"]
# result = enumerate(list1 , 5)
# print(list1(result))
#
list2 = ["ironman" , "hulk" , "thor" , "capaitan"]
i = 0
for item in list2:
    if i % 2 != 0 :
        print(f"hero {item}")
    i = i + 1

for index,item in enumerate(list2, 0):
    if index % 2 == 0 :
        print(f" index is {index} and  hero is {item}")
    i = i + 1