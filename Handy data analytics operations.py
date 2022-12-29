import numpy as np

# Operations that come in handy for data analysis
one_dim = np.array([1, 2, 3, 4, 5])
two_dim = np.array([[1, 2, 3], [4, 5, 6]])

# Summations
print(sum(one_dim))
print(sum(two_dim))  # Adding first element to the second element of array
print(one_dim.sum())
print(two_dim.sum())  # Total sum of all the elements in two arrays.

# Maximum and minimum
print(one_dim.min())
print(two_dim.max())

# We can add elements in each row and column
# Summing elements within each column
two_dim2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(two_dim2.sum(axis=0))  # taking the columns and adding like 1+4+7
# axis = 0 for column ; axis = 1 for row
# Summing elements within each row
two_dim2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(two_dim2.sum(axis=1))
