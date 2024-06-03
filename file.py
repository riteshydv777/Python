# file  IO

""""" r / rt : mode of opening file only reading.

        read(): read file."""
#
# f = open("file.txt","r")
# print(f.read())
# f.close()
# print(" ")
#
# f = open("file.txt", "r")
# Content = f.read()
# print(Content)
# f.close()

"""  readline(): open only one sentence in txt file. """
#
# f = open("file.txt","r")
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()

"""  readlines(): print list of our file """
#
# f = open("file.txt","r")
# print(f.readlines())
# f.close()


""" w : mode of opening file for writing.
 write mode
          write():write in file."""
#
# f = open("file.txt","w")
# f.write("I am from Bihar \n")
#
# f.close()
#
# f = open("file1.txt","w")  # create new file1.txt and write.
# f.write("I am from Bihar \n")
# f.close()

"""append mode.--> open multiple time same sentencec."""
#
# f = open("file1.txt","a")
# f.write("I am from Bihar \n")
# a = f.write("I am from Bihar ")
# print(a)

""" seek() , tell() function."""
#
# f = open("file.txt","r")
# f.seek(7)
# print(f.read())
# f.close()
#
# f = open("file.txt","r")
# print(f.tell())
# print(f.readline())
#
# print(f.tell())
# print(f.readline())
#
# f.close()
