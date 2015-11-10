
#sortings

def merge(L,R):
	i=0
	j=0
	new=[]
	while i<len(L) and j<len(R):
		if L[i]<R[j]:
			new.append(L[i])
			i+=1
		else:
			new.append(R[j])
			j+=1
	if i<len(L):
		new.extend(L[i:])
	if j<len(R):
		new.extend(R[j:])
	return new
def merge_sort(A):
	n=len(A)
	if n==1:
		return A
	else:
		middle=n//2
		L=merge_sort(A[:middle])
		R=merge_sort(A[middle:])
		return merge(L,R)


def quick_sort(A,low,high):
        if low<high:
                p=partition(A,low,high)
                quick_sort(A,low,p-1)
                quick_sort(A,p+1,high)
def partition(A,low,high):
        pivot=A[high]
        i=low-1
        for j in range(low,high+1):
                if A[j]<=pivot:
                        i+=1
                        A[i],A[j]=A[j],A[i]
        return i


def bubble(A):
        n=len(A)
        for i in range(n):
                flag=0
                for j in range(n-i-1):
                        if A[j]>A[j+1]:
                                A[j],A[j+1]=A[j+1],A[j]
                                flag=1
                if flag==1:
                        break

def insertion(A):
        n=len(A)
        for i in range(n):
                for j in range(i):
                        if A[i]<A[j]:
                                A[i],A[j]=A[j],A[i]

def selection(A):
        n=len(A)
        for i in range(n):
                max=i
                for j in range(n-i):
                        if A[max]<A[j]:
                                max=j
                A[i],A[max]=A[max],A[i]

#array implementation of stack and que

class stack(object):
        def __init__(self):
                self.list=[]
        def push(self,key):
                self.list.append(key)
        def pop(self):
                return self.list.pop()
        def is_empty(self):
                return self.list==[]
class que(object):
        def __init__(self):
                self.list=[]
        def enque(self,key):
                self.list.append(key)
        def deque(self):
                x=self.list[0]
                del(self.list[0])
                return x
        def is_empty(self):
                return self.list==[]
#stack using que and que using stack
class que1(object):
        def __init__(self):
                self.s1=stack()
                self.s2=stack()
        def enque(self,key):
                self.s1.push(key)
        def deque(self):
                if self.s2.is_empty()==True:
                        while not self.s1.is_empty():
                                self.s2.push(self.s1.pop())
                        return self.s2.pop()
        def is_empty(self):
                return self.s1.is_empty() and self.s2.is_empty()
class stack1(object):
        def __init__(self):
                self.q1=que()
                self.q2=que()
        def push(self,key):
                self.q2.enque(key)
                while self.q1.is_empty()==False:
                        self.q2.enque(self.q1.deque())
                temp=que()
                temp=self.q1
                self.q1=self.q2
                self.q2=temp
        def pop(self):
                return self.q1.deque()
#linked list
class llnode(object):
        def __init__(self,key):
                self.key=key
                self.next=None
        def insert(self,node):
                if self.next==None:
                        self.next=node
                else:
                        self.next.insert(node)


        













        

                        
