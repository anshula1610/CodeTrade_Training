# Task 8: Build and Inspect NumPy Arrays, then Slice Them
# Demonstrates array creation, inspection, indexing, and slicing.

import numpy as np

# ----------------------------------
# Create Arrays
# ----------------------------------

arr1 = np.array([10, 20, 30, 40, 50])

arr2 = np.arange(1, 11)  # 1 to 10

arr3 = np.zeros((2, 3))

arr4 = np.linspace(0, 100, 5)

# ----------------------------------
# Print Arrays
# ----------------------------------

print("Array 1:")
print(arr1)

print("\nArray 2:")
print(arr2)

print("\nArray 3:")
print(arr3)

print("\nArray 4:")
print(arr4)

# ----------------------------------
# Inspect Arrays
# ----------------------------------

print("\n=== Array Inspection ===")

print("\narr1")
print("Shape:", arr1.shape)
print("Data Type:", arr1.dtype)
print("Dimensions:", arr1.ndim)

print("\narr3")
print("Shape:", arr3.shape)
print("Data Type:", arr3.dtype)
print("Dimensions:", arr3.ndim)

# ----------------------------------
# Indexing
# ----------------------------------

print("\n=== Indexing ===")

# First element
print("First element of arr1:", arr1[0])

# Negative index (last element)
print("Last element of arr1:", arr1[-1])

# ----------------------------------
# Slicing
# ----------------------------------

print("\n=== Slicing ===")

# Returns a subarray
print("Elements from index 1 to 3:")
print(arr1[1:4])

# Slice from index 3 to end
print("Elements from index 3 onward:")
print(arr1[3:])

# Every second element
print("Every second element:")
print(arr1[::2])