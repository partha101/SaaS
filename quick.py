def quick_sort(A,low,high):
	if low<high:
		p=partition(A,low,high)
		quick_sort(A,low,p-1)
		quick_sort(A,p+1,high)
	for i in A:
		print i
def partition(A,low,high):
	pivot = A[high]
    	i = low #place for swapping
    	for j in range(low,high):
        	if A[j] <= pivot:
            		A[i],A[j]=A[j],A[i]
            		i = i + 1
    	A[i],A[high]=A[high],A[i]
    	return i
A=[12,23,1,222,43]
quick_sort(A,0,4)


