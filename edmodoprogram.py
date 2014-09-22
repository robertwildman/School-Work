#This program will get the name and afes of five people and then will sort highest to lowest
def Main():
	#This will get the name and ages using the Getinput Fucntion.
	names = getinput("Name","a")
	ages = getinput("Ages",names)
	#It will then use a bubblesort to sort the names and ages.
	BubbleSort(ages,names,len(ages))
	#
	print ages
	print names

#This is a bubble sort and will sort an array from lowest to highest
def BubbleSort(ages,names,n):
    #Will get the size of the array and will loop around for the size
    for i in xrange(0, n-1):
    	sorted = True
    	for j in xrange(0, n-1-i):
			#Will see if the one above is grater if so it will swap them around.
			if ages[j] > ages[j+1]:
				temp = ages[j]
				ages[j] = ages[j+1]
				ages[j+1] = temp
				temp1 = names[j]
				names[j] = names[j+1]
				names[j+1] = temp1
				sorted = False
				if sorted == True:
			#When fully sort it will break the loop.
			break

[#Name],[Age],[Address]
#This will ask the user for 5 name and then ask for 5
def getinput(inputtype,namearray):
	if inputtype == "Name":
		names = []
		for i in range (0,5):
			names.append(raw_input("Please enter the name of person number "+str(i)+" :    "))
			return names

			if inputtype == "Ages":
				ages = []
				for i in range (0,5):
					ages.append(raw_input("Please enter the age of "+namearray[i]+":   "))
					return ages

					Main()