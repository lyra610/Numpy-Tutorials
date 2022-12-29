import numpy as np
# Higher dimensions, each array  should have same number of elements
# ie, [[1,2,3,4],[5,6,7]] is wrong
# ie, [[1,2,3,4],[5,6,7,8]] is right
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])
# joining arrays. Concatenating these two arrays together
joined_array = np.concatenate((array1, array2))
print(joined_array)

# join along rows
array3 = np.array([[1, 2, 3], [4, 5, 6]])
array4 = np.array([[7, 8, 9], [10, 11, 12]])
join = np.concatenate((array3, array4))
print(join)
# If we do not specify along which axis we have to join. It will be column
# Since axis of column is 0
# axis=1;rows and axis=2;columns
joined_row_array = np.concatenate((array3, array4), axis=1)
print(joined_row_array)

# Joining columns. axis=0 is for columns
joined_column_array = np.concatenate((array3, array4), axis=0)
print(joined_column_array)

# Joining 3-Dimensional arrays
array5 = np.array([2, 4, 6, 8, 20], ndmin=3)  # Creating the array 3 dimensional using ndmin
array6 = np.array([1, 3, 5, 7, 9], ndmin=3)
joining_3dim = np.concatenate((array5, array6))
print(joining_3dim)

# splitting arrays
arr = np.array([1, 2, 3, 4, 5, 6])  # one dimensional array
split_array = np.array_split(arr, 2)
# numpy has a specific function for splitting np.array_split
print(split_array)
print(split_array[0])  # print [1,2]
