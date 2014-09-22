array = []
array_size = raw_input("Please enter the size of the array")
for number in range(0,int(float(array_size))):
	user_input = raw_input("Please enter the %number of the array")
	array.append(user_input)

def Counting(array,search_term):
	count = 0
	for x in array:
		if x == search_term:
			count = count + 1
	print count

Counting(array,raw_input("Please enter the search term"))
