#This will take a sort array and also a search term. 
def Selection_Sort(a):
  for i in range(0,len(a)-1):
	for j in range(i+1,len(a)):
		if a[i] > a[j]:
				temp = a[j]
				a[j] = a[j+1]
				a[j+1] = temp
  print a
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
Selection_Sort(a)

choice = raw_input("Quit?")
if choice == 'q':
	exit() 	