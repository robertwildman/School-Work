#This is a bubble sort and will sort an array from lowest to highest
def BubbleSort(a,n):
    #Will get the size of the array and will loop around for the size
    for i in xrange(0, n-1):
		sorted = True
		for j in xrange(0, n-1-i):
			#Will see if the one above is grater if so it will swap them around.
			if a[j] > a[j+1]:
				temp = a[j]
				a[j] = a[j+1]
				a[j+1] = temp
				sorted = False
		if sorted == True:
			#When fully sort it will break the loop.
			break
    return a
a = [5,7,3,7,9,2,6,3,8,6,4,6,7]
print BubbleSort(a,len(a))
