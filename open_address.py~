#the following programme is for open addressing hash
def h1(x):
	return x%2**8
def h2(x):
	index=x%2**8
	if index%2==0:
		return index+1
	else :
		return index
def h(x,i):
	return (h1(x)+(i*h2(x)))%2**8
class open_address(object):
	def __init__(self):
		self.list=[]
		for i in range(0,2**8):
			self.list.append(None)
	def insert(self,key):
		for i in range(0,2**8):
			if h(key,i)==None or h(key,i)=="delete me":
				self.list[i]=key
				break
	def search(self,key):
		for i in range(0,2**8):
			if h(key,i)==None:
				print "element not found"
	def delete(self,key):
		for i in range(0,2**8):
			if self.list[h(key,i)]==key:
				self.list[h(key,i)]="delete me"
				break
			elif self.list[h(key,i)]==None:
				print "item not found"
	def print_list(self):
		for  i in self.list:
			if i!=None or i!="delete me":
				print str(i)+" "
x=input("enter number of elements to be stored\n")
op=open_address()
for i in range(x):
	z=input()
	op.insert(z)
num=input("enter the elemnt to be deleted\n")
op.delete(num)
op.print_list()	
			

