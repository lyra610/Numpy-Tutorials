# Importing relevant modules
import numpy as np

# In NumPy, we have a function called 'sort'.
# This will sort the arrays in mathematical order
array1 = np.array([1, 75, 82763, 364, 4721, -327, -23736])
array1_sorted = np.sort(array1)
print(array1, array1_sorted)

# Sorting 2-dimensional arrays
array2 = np.array([[-273, -27, 56, 23], [-23, 98, 263, 522]])
# Higher dimensions, each array  should have same number of elements
# ie, [[1,2,3,4],[5,6,7]] is wrong
# ie, [[1,2,3,4],[5,6,7,8]] is right
array2_sorted = np.sort(array2)
print(array2_sorted)  # Sort elements in each array. Not as total

# We don't just need to have numbers to sort in arrays
boolean_array = np.array([True, False, False, True, False, True, False])
boolean_array_sorted = np.sort(boolean_array)
print(boolean_array_sorted)

# Sorting array of strings into alphabetical order
string_array = np.array(['Oslo', 'Trondheim', 'Trømso', 'Bergen', 'Stavanger'])
string_array_sorted = np.sort(string_array)
print(string_array_sorted)  # Sorting on basis of first letter!

# Another cool function in NumPy - 'searhsorted'.
# This command will return index where the inputted value
# would need to be placed, inorder to maintain the order
array3 = np.array([1, 2, 3, 5, 6])
location = np.searchsorted(array3, 4)
print(location)  # Tell which location we have to place 4

# We can also give list of numbers and ask where will put those in the array
location1 = np.searchsorted(array3, [10, 2, 8])
print(location1)
