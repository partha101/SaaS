from build_max_heap import build_max_heap
from build_max_heap import max_heapify
class heap:
	def __init__(self):
		self.list=[]
	def insert(self,x):
		self.list.append(x)
		build_max_heap(self.list)
	def is_empty(self):
		return self.list==[]
	def extract_max(self):
		self.list[len(self.list)-1],self.list[0]=self.list[0],self.list[len(self.list)-1]
		print self.list.pop()
		build_max_heap(self.list)
	def heap_sort(self):
		while not self.list.is_empty():
			extract_max()
	def delete(self):
		self.list.pop()
	def delete_item(self,k):
		for i in self.list:
			if i==k:
				index=self.list.index(i)
				break
		self.list[len(self.list)-1],self.list[index]=self.list[index],self.list[len(self.list)-1]
		self.list.pop()
		build_max_heap(self.list)
	def print_list(self):
		for i in self.list:
			print i
	def change_key(self,i,key):
		if key<self.list[i]:
			print "no insertion"
		else :
			self.list[i]=key
			build_max_heap(self.list)
		
			
heap1=heap()
x=input("enter the number of elements to be stored\n")
new=[]
print "enter the numbers\n"
for i in range(x):
	new.append(input())
for i in new:
	heap1.insert(i)
x=raw_input("enter delete if you want to delete the max element or change if you want to change some key\n")
if x=="delete":
	heap1.extract_max()
elif x=="change":
	i,k=input("enter the index i you want to change with the key k in the form i,k\n")
	heap1.change_key(i,k)
else :
	print "invalid input"
	
heap1.print_list()	
		
					
