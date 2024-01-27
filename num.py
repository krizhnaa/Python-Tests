import numpy as np

arr1 = np.linspace(1, 10, 9).reshape((3,3))
arr2 = np.arange(36, 45).reshape((3, 3))

print(arr1.resize(3,3))
# print(arr1[:, :])
# print(arr2)