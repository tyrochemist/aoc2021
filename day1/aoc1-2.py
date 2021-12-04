from numpy import genfromtxt

#Input CSV as array via numpy dataframe
depths = genfromtxt('input.csv')
oldSum = 0
newSum = 0
increases = 0
newest = 0
middle = 0
oldest = 0
#enumerate through depths
for count, depth in enumerate(depths):
    #get value from string
    depthVal = int(depth)
    #Shuffle over values in "memory"
    oldest = middle
    middle = newest
    newest = depthVal
    if count > 2:
        newSum = oldest + middle + newest
        if newSum > oldSum and oldSum != 0:
            increases += 1
    oldSum = newSum

print('The comparison increased {} times.'.format(increases))