# wap for numpy array properties and function.
import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60]])

print("Array:")
print(arr)

print("\nArray Properties:")
print("Number of dimensions:", arr.ndim)
print("Shape of array:", arr.shape)
print("Total number of elements:", arr.size)
print("Data type:", arr.dtype)

print("\nNumPy Functions:")
print("Maximum value:", np.max(arr))
print("Minimum value:", np.min(arr))
print("Sum of elements:", np.sum(arr))
print("Mean of elements:", np.mean(arr))
print("Square root:")
print(np.sqrt(arr))
