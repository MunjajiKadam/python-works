import numpy as np 
import pandas as pd

arr = np.array([[1, 2, 3], ["mk", "satish", "gaurav"], [22, 23, 90]])
print("Original array:")
print(arr)
print("Array statistics:")
# print("Max:", arr.max())
print("Min:", arr.min())
print("Sum:", arr.sum())
print("Mean:", arr.mean())
print("Standard Deviation:", arr.std())
print("Variance:", arr.var())
print("Shape:", arr.shape)
print("Number of dimensions:", arr.ndim)
print("Size:", arr.size)
print("Data type:", arr.dtype)
print("Item size:", arr.itemsize)
print("Transposed array:")
print(arr.T)
print("Flattened array:")
print(arr.flatten())



dataframe = pd.DataFrame(arr, columns=['rollno', 'name', 'age'])
print("\nDataFrame:")
print(dataframe)