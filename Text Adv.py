#This program will make a 3 x 3 room and then will allow the user to walk around the room
elements = []
def main():
	#This will start up the program and functions
	print "Hello and Welcome!"
	print "Heres the map:"
	global elements
	elements.append([])
	elements.append([])
	elements.append([])
	elements[0].append(1)
	elements[0].append(2)
	elements[0].append(3)
	elements[1].append(4)
	elements[1].append(5)
	elements[1].append(6)
	elements[2].append(7)
	elements[2].append(8)
	elements[2].append(9)
	#This prints out the room map.
	print "[1],[2],[3]"
	print "[4],[5],[6]"
	print "[7],[8],[9]"
	#Starts new room at cord.
	newroom(0,0)

def newroom(x,y):
	#This will start when your in a new room.
	print "You are now in room: " + str(elements[y][x])
	direction = raw_input("Please now move if W,A,S,D or Q:  ")
	print ""
	if(direction.lower() == "q"):
		exit()
	elif (direction.lower() == "w" or direction.lower() == "a" or direction.lower() == "s" or direction.lower() == "d"):
		changeroom(x,y,direction.lower())
	else:
		print "Incorrect key please enter W,A,S,D"

def changeroom(startx,starty,direction):
	#This will change in room if the x or y is in between the 0 - 2 if not error message
	if (direction.lower() == "w"):
		#Moving up
		y = starty + 1
		x = startx
	elif (direction.lower() == "a"):
		#Moving Left
		x = startx - 1
		y = starty
	elif (direction.lower() == "s"):
		#Moving Down
		y = starty - 1
		x = startx
	elif (direction.lower() == "d"):
		#Moving Right
		x = startx + 1
		y = starty


	if(x > 2 or x < 0 or y > 2 or y < 0):
		#The user is out of bounds
		print "Sorry there is no room here please try again"
		print ""
		newroom(startx,starty)
	else:
		#User is in a room
		#Will return room number
		newroom(x,y)


main()