import numpy as np

# we can create an array between like we can do with
# list and range command
# when using aray we use arrange command
# this will produce number to 10 but not 10
a = np.arange(0, 5)
print(a)
# basic mathematical operations of arrays
b = np.array([4, 6, 23, 45, 78])
print(b)
# adding
print(a + b)  # Add each element with others.
# Notice that size of the 2 arrays are same
print(a.shape, b.shape)
print('Square of a =', a ** 2, ',', 'Square of b =', b ** 2)

print(np.sqrt(a ** 2))  # we have square root functions in numpy

# multiplying everything in a by 3
print(a * 3)

# Testing whether values in array is less than certain value
c = np.array([1, 2, 3, 4])
print(c > 2)
