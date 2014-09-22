#Xfactor Program. Will ask the user ot enter in there name , age and address
def main():
	#This function will work out if the user is an admin or constant
	getrole()

def saveperson(name,age,address):
	#This function is used to save to the file
	filename = "Xfactorprefs.txt"
	f = open(filename,"a")
	f.write(name+","+age+","+address+'\n')
	f.close()

def savesort(names,ages,addresss):
	#This function is used to save to the file
	filename = "Xfactorprefs.txt"
	f = open(filename,"w")
	for i in range(0,len(names)):
		f.write(names[i]+","+ages[i]+","+addresss[i]+'\n')
	f.close()

def read():
	#This function is used to read the array it will first clear the array then it will read into the array
	namearray=[]
	agearray=[]
	addressarray=[]
	filename = "Xfactorprefs.txt"
	f = open(filename,"r+")
	for i in f:
		TempString = i
		Temparray = TempString.split(',')
		namearray.append(Temparray[0])
		agearray.append(Temparray[1])
		Addressstring = Temparray[2].split('\n')
		addressarray.append(Addressstring[0])
	f.close
	print namearray
	print agearray
	print addressarray

def readtobubble():
	#This will read the program and then start the program
	#This function is used to read the array it will first clear the array then it will read into the array
	namearray=[]
	agearray=[]
	addressarray=[]
	filename = "Xfactorprefs.txt"
	f = open(filename,"r+")
	for i in f:
		TempString = i
		Temparray = TempString.split(',')
		namearray.append(Temparray[0])
		agearray.append(Temparray[1])
		Addressstring = Temparray[2].split('\n')
		addressarray.append(Addressstring[0])
	f.close
	BubbleSort(agearray,addressarray,namearray,len(agearray))


def readtosearch():
	#This will read the program and then start the program
	#This function is used to read the array it will first clear the array then it will read into the array
	namearray=[]
	agearray=[]
	addressarray=[]
	filename = "Xfactorprefs.txt"
	f = open(filename,"r+")
	for i in f:
		TempString = i
		Temparray = TempString.split(',')
		namearray.append(Temparray[0])
		agearray.append(Temparray[1])
		Addressstring = Temparray[2].split('\n')
		addressarray.append(Addressstring[0])
	f.close
	Name = raw_input("Please Enter the name you wish to search:  ")
	Search(Name,namearray,agearray,addressarray)


def conmain():
	exit = False
	while(exit == False):
		name = raw_input("Please enter your name? ")
		age = raw_input("Please enter your age? ")
		address = raw_input("Please enter your Address? ")
		saveperson(name,age,address)
		exitinfo = raw_input("Would u like to enter another contestant? (Y)es or (N)o ")
		if(exitinfo.lower() == "n"):
			exit = True
	getrole()
	#This function will deal with the input of user data.

def adminmain():
	#This function will deal with admin uses.
	#This calls the read function to read the saved file.
	read()
	Answer = raw_input("Would you like to sort or search?   ")
	if (Answer.lower() == "sort"):
		#This will deal with the searching.
		readtobubble()
		getrole()
	elif(Answer.lower() == "search"):
		#This will read it and then it will search it
		readtosearch()
		getrole()





#This is a bubble sort and will sort an array from lowest to highest
def BubbleSort(ages,address,names,n):
    #Will get the size of the array and will loop around for the size
	print names
	print ages
	print address
	print n
	for i in xrange(0, n-1):
		for j in xrange(0, n-1-i):
			if ages[j] > ages[j+1]:
				#Deals with the moving of Ages
				temp = ages[j]
				ages[j] = ages[j+1]
				ages[j+1] = temp
				#Deals with moving of Names
				temp1 = names[j]
				names[j] = names[j+1]
				names[j+1] = temp1
				#Deaks with moving of address
				temp2 = address[j]
				address[j] = address[j+1]
				address[j+1] = temp2

	savesort(names,ages,address)
	print names
	print ages
	print address


#This will take a sort array and also a search term.
def Selection_Sort(ages,address,names):
  	for i in range(0,len(ages)-1):
		for j in range(i+1,len(ages)-1):
			if ages[i] > ages[j]:
				temp = ages[j]
				ages[j] = ages[j+1]
				ages[j+1] = temp
				#Deals with moving of Names
				temp1 = names[j]
				names[j] = names[j+1]
				names[j+1] = temp1
				#Deaks with moving of address
				temp2 = address[j]
				address[j] = address[j+1]
				address[j+1] = temp2

	getrole()

def Search(Name,namearray,agearray,addressarray):
	print "Starting to search"
	for i in xrange(0,len(namearray)):
		if(namearray[i] == Name):
			print "Name: " + namearray[i]
			print "Age: "agearray[i]
			print ""addressarray[i]

def getrole():
	#This function will get what role the user is.
	answer = raw_input("If your a contestants enter C If your an Admin enter A and enter Q to Quit:   ")
	if(answer.lower() == "c"):
		conmain()
	elif(answer.lower() == "a"):
		adminmain()
	elif(answer.lower() == "q"):
		quit()

def nothing():
	print ""

main()
