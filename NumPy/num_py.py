import numpy as np


print("Example 1D arrays")
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print("Array Slicing: ", arr[1:5])
print("Array Slicing: ", arr[4:])
print("Array Slicing: ", arr[:4])
print("Array Slicing: ", arr[1:5:2])
print("Array Slicing: ", arr[::2])

print("Example 2D arrays")
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr1:
    for y in x:
        print(y)
print(arr1)
print("2nd element on 1st row: ", arr1[0, 1])

print("Example 3D arrays")
arr2 = np.array([[[1, 2, 3], [4, 5, 6]] , [[1, 2, 3], [4, 5, 6]]])
print(arr2)


print("Creating Arrays with a Defined Data Type..")
arr3 = np.array([1, 2, 3, 4], dtype='S')
print(arr3.dtype)


print("Numpy Array copy and View..")
array1 = np.array([1, 2, 3, 4, 5])
x = array1.copy()
array1[0] = 45
print(array1)
print(x)

print("Make a view, change the original array, and display both arrays: ")
array2 = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)

print("Array sorting")
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))
