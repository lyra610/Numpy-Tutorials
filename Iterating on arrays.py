import numpy as np
# Higher dimensions, each array  should have same number of elements
# ie, [[1,2,3,4],[5,6,7]] is wrong
# ie, [[1,2,3,4],[5,6,7,8]] is right
# Iterating over one - dimensional array
one_dim = np.array([1, 2, 3, 4, 5])
for element in one_dim:
    print(element)

# Creating a 2-dimensional array
two_dim = np.array([[1, 2, 3], [4, 5, 6]])
for element in two_dim:
    print(element)  # Each element is one single array in two dim
# Output will be [1,2,3] [4,5,6]

# To get every single elements of the array
for element in two_dim:
    for number in element:
        print(number)

# Using 'nditer'
# A very good way of iterating without many for loops!!!
for element in np.nditer(two_dim):
    print(element)

# Figuring out the index
for index, element in np.ndenumerate(two_dim):
    print(index, element)

