# Importing relevant modules
import numpy as np

# We can search in a given array and say whether the element is located there!

# One dimensional array
array1 = np.array([1, 2, 3, 4, 4, 6, 8, 9, 9, 8])
# Finding the location of the values in this array!
location = np.where(array1 == 4)
print(location)
# This prints '(array([0], dtype=int64),)' and tells us that, number 4 is
# located in the index 3 and 4. Thy dtype just mentions the data type

# You can more than just locate the elements in the array :)
less_than_five = np.where(array1 <= 5)
print(less_than_five)

# To find the elements divisible by 3
divisible_by_3 = np.where(array1 % 3 == 0)
print(divisible_by_3)
