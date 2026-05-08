import numpy as np

# Task 1
arr1d = np.array([10, 20, 30, 40, 50])
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("1D array:", arr1d)
print("2D array:\n", arr2d)

# Task 2
print("\n2nd element of 1D:", arr1d[1])
print("Element at 2nd row 3rd col:", arr2d[1, 2])

# Task 3
arr2d[0, 0] = 99
print("\nModified 2D array:\n", arr2d)

# Task 4
print("\nMax of 1D:", np.max(arr1d))
print("Min of 1D:", np.min(arr1d))
print("Sum of 2D:", np.sum(arr2d))

# Task 5
arr12 = np.arange(1, 13)
print("\nOriginal:", arr12)
print("3x4:\n", arr12.reshape(3, 4))
print("2x6:\n", arr12.reshape(2, 6))

# Task 6
a = np.array([[1, 2, 3], [4, 5, 6]])
print("\nOriginal:\n", a)
print("flatten():", a.flatten())
print("ravel():", a.ravel())

# Task 7
m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nMatrix:\n", m)
print("Elements:")
for row in m:
    for x in row:
        print(x)

# Task 8
a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
print("\nJoined 1D:", np.concatenate((a1, a2)))

b1 = np.array([[1, 2], [3, 4]])
b2 = np.array([[5, 6], [7, 8]])
print("Joined rows:\n", np.concatenate((b1, b2), axis=0))
print("Joined cols:\n", np.concatenate((b1, b2), axis=1))

# Task 9
s = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("\nSplit 1D:", np.split(s, 3))

d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print("Split rows:", np.split(d, 2, axis=0))
print("Split cols:", np.split(d, 2, axis=1))

# Task 10
r = np.array([12, 45, 67, 23, 89, 34, 78])
print("\nArray:", r)
idx = np.where(r > 50)
print("Indices > 50:", idx[0])
print("Values:", r[idx])