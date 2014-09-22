import math
#This will take a sort array and also a search term.
def binarySearch(a,searchterm):
  Endpoint = len(a)
  Startpoint = 1
  Found = False
  while(Found == False):
    Middlepoint = int(math.floor((Startpoint + Endpoint) / 2))
    if Startpoint >= Endpoint:
        print "Number was not found the array!"
        break
    elif a[Middlepoint] == searchterm:
        print Middlepoint
        Found = True
        return Middlepoint
    elif a[Middlepoint] < searchterm:
    	Startpoint = Middlepoint + 1
    else:
		Endpoint = Middlepoint - 1
  return 0

a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
binarySearch(a,16)
