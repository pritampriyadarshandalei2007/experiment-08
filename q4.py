# wap for statistical operations and broadcasting on arrays.
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)

print("\nStatistical Operations:")
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))

print("\nBroadcasting:")

result1 = arr + 5
print("Array + 5:", result1)

result2 = arr * 2
print("Array * 2:", result2)

