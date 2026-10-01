# wap for saving and loading arrays.
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Original Array:")
print(arr)

np.save("myarray.npy", arr)
print("\nArray saved successfully.")

new_arr = np.load("myarray.npy")
print("\nLoaded Array:")
print(new_arr)

