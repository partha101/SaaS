def insertion(list):
	n=len(list)
	for i in range(0,n):
		for j in range(0,i):
			if list[i]<list[j]:
				temp=list[i]
				list[i]=list[j]
				list[j]=temp
	for i in list:
		print str(i)+" "
n=input("enter the number of elements to be sorted")
list1=[]
for i in range(0,n):
	x=input()
	list1.append(x)
insertion(list1)

	
