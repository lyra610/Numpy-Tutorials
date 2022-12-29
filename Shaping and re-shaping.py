import numpy as np

# shape of an array
array = np.array([[1, 2, 3, 10], [4, 5, 6, 10], [7, 8, 9, 34]])
print(array.shape)  # gives the shape of the array. we have 3 elements inside and inside
# that we have 4 elements

# array2=np.array([[1,2,3], [1,2,3,4]])
# print(array2.shape) #this will give error because shape command doesnt work is
# elements inside arrays are of different shape

students = np.array([19, 19, 19, 20, 20, 20, 21, 21, 21])
exam_score = np.array([57, 60, 32, 59, 63, 70, 45, 89, 38])
# reshaping the array. Splitting up the exam score
exam_split = exam_score.reshape(3, 3)
print(exam_split)  # now we get scores for age 19,20,21 separately

# we can't reshape every single array
# for example we cannot reshape like reshape.(2,3)
# INPUT INTO RESHAPE COMMAND MUST MULTIPLY TOGETHER TO CREATE THE
# NUMBER OF ELEMENTS IN THE ORIGINAL ARRAY

# reshape 3 dimensional array
one_dim = np.array([1, 2, 3, 4, 5, 6])
three_dim = one_dim.reshape(2, 3, 1)  # INPUT INTO RESHAPE COMMAND MUST MULTIPLY TOGETHER TO CREATE THE
# NUMBER OF ELEMENTS IN THE ORIGINAL ARRAY
print(three_dim)
