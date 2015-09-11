def merge_sort(list):
    if len(list)==1:
        return list
    else:
        n=len(list)
        middle=n//2
        L=merge_sort(list[:middle])
        R=merge_sort(list[middle:])
        print merge(L,R)



def merge(L,R):
    i=0
    j=0
    new=[]
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            new.append(L[i])
            i+=1
        else :
            new.append(R[j])
            j+=1
    if i<len(L):
        new.extend(L[i:])
    if j<len(R):
        new.extend(R[j:])
    return new

n=input("enter the number of terms to be stored")
new=[]
for i in range(0,n):
    x=input()
    new.append(x)
merge_sort(new)

    
