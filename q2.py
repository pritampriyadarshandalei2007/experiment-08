# wap for Data types and structures in numpy.
import numpy as np

a = np.array([10, 20, 30])
b = np.array([1.5, 2.5, 3.5])
c = np.array(["Apple", "Banana", "Mango"])

print("Integer Array:", a)
print("Data type:", a.dtype)

print("\nFloat Array:", b)
print("Data type:", b.dtype)

print("\nString Array:", c)
print("Data type:", c.dtype)

arr1 = np.array([10, 20, 30, 40])
print("\n1-D Array:", arr1)

arr2 = np.array([[1, 2], [3, 4]])
print("2-D Array:")
print(arr2)

arr3 = np.array([[[1, 2], [3, 4]],
                 [[5, 6], [7, 8]]])
print("3-D Array:")
print(arr3)
