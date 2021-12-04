from numpy import genfromtxt

#Input CSV as array via numpy dataframe
depths = genfromtxt('input.csv')
oldDepth = 0
increases = 0

#loop through depths, convert to ints and compare with last depth, noting increases
for depth in depths:
    depthVal = int(depth)
    if depthVal > oldDepth and oldDepth != 0:
        increases += 1
    oldDepth = depthVal

print('The depth increased {} times.'.format(increases))