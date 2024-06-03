import time

# time.time() function to get the current time in seconds since the epoch, and then printed the result.

seconds = time.time()
print("seconds since epoch = " , seconds)
time.asctime()

initial1  = time.time()
print("tony:")
time.sleep(5)
print("excution time :" , time.time() - initial1 , "seconds" )
print("tony")

for i in range(11):
    print("jai mata di")
    time.sleep(1)

initial = time.time()
k = 0
while( k < 5):
    print("jai mahakaal")
    time.sleep(2)
    k = k + 1
print("loop run in " , time.time() - initial , "seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)