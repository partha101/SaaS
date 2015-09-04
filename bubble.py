def bubble(list):
	n=len(list) 
	for i in range(0,n):
		for j in range(0,n-i-1):
			if list[j]>list[j+1]:
				temp=list[j]
				list[j]=list[j+1]
				list[j+1]=temp
	for i in list:
		print str(i)+" "
n=input("enter the number of terms to be sorted")
list=[]
for i in range(0,n):
	x=input()
	list.append(x)
bubble(list)

				
