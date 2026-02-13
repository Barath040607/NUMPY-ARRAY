import numpy as np

# Create arrays
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print("Array a:", a)
print("Array b:", b)

# Element-wise operations
print("\nAddition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Reshape array
matrix = a.reshape(2, 2)
print("\nReshaped a into 2x2 matrix:")
print(matrix)

# Create another matrix
m2 = np.array([[1, 2], [3, 4]])

# Matrix multiplication
result = matrix @ m2
print("\nMatrix multiplication result:")
print(result)

# Aggregations
print("\nSum of a:", a.sum())
print("Mean of a:", a.mean())
print("Max of a:", a.max())

# Boolean indexing
print("\nElements greater than 2:", a[a > 2])

# Random array
np.random.seed(0)
random_array = np.random.randint(1, 10, size=(3, 3))
print("\nRandom 3x3 array:")
print(random_array)
