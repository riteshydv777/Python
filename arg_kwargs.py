import time

def fun_name(a,b,c):
      print(a,b,c)

fun_name("tony" , "jack" ,"jenny")

# ......args example .....

# def fun_args(*args):
#     print(type(args))
#
#     print(args[2])
#
#     for item in args:
#         print(item, end = " ")
#
# channel = ["starplus" , "zeetv" , "pogo" , "cartoon"]
# fun_args(*channel)



def function1(normal , *args , **kwargs):
    print(type(args))

    for item in args:
        print(f" our main avenger {item}")

    print()
    print("our heros identity : ")
    print()
    for key , value in kwargs.items():
        print(f"{key} is  {value}")



ar = ["ironman" , "hulk" , "thor" , "captain"]
normal = "these are avengers : "
kw = {"ironman":"tony",
       "hulk" : "doctor",
       "thor" : "asgurd",
        "captain" : "old hero"}

function1(normal, *ar, **kw)








