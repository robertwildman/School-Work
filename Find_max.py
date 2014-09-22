def  find_max(array):
    max = array[0]
    for x in array:
        if x > max:
            max = x
    print max


find_max([3,4,5,6,1])