import heap
import random
import time
time=time.time
random=random.random
heap=heap.heap
x=input("enter the number of elements to be stored in the array")
list=[]
for i in range(0,x):
	list.append(random())
heap1=heap()
for i in list:
	heap1.insert(i)
start=time()
while not heap1.is_empty():
	heap1.extract_max()
print "time taken is "+str(time()-start)
