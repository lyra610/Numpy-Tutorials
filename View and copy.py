import numpy as np

# copy
array = np.array([1, 2, 3, 4, 5])
copy = array.copy()  # copy of the original array
print(copy)
array[0] = 11
print([array, copy])  # copy will not change the later changes made in the array

# view
array2 = np.array([1, 2, 3, 4, 5])
array2[0] = 11
view = array2.view()
print([view, array2])  # while copy remains the same, view does not. View is also changing

#python to recall whether its a copy or view
print(view.base)
print(copy.base)