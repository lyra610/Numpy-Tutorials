# slicing the arrays
import numpy as np

# you should always say np.array while assigning a numpy array. Otherwise, it will be a tuple
one_dim = np.array([1, 2, 3, 4, 5])  # one dimensional arrays
print(one_dim[0:3])  # we will get 1,2,3 but not 4.
print(one_dim[:])
print(one_dim[:4:2])

two_dim = np.array([[1, 2, 3], [4, 5, 6]])
print(two_dim[1, 0:2])  # end 2 means it will count from 0,1 . its -1 value that prints

# creating another 2 dimensional array
two_dim_2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(two_dim_2[0:2, 0])  # first part says which array you need so we get
# elements from 0 and ist arrays. in that we get first elements
print(two_dim_2[0:3, 0:3:2])
