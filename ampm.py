x=raw_input()
list1=x.split(":")
list2=list(list1[2])
if list2[2]=="p" or list2[2]=="P":
	a=int(list1[0])+12
	if a==24:
		a=0
else :
	print list1[0]+":"+list1[1]+":"+list1[2][0]+list1[2][1]
print str(a)+":"+list1[1]+":"+str((int(list2[0])*10)+int(list2[1]))

