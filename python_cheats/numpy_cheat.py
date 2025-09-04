import numpy as np

# np.array
arr = np.array([[3,2,9],[1,5,1],[0,3,4]])

# np.zeros
zeros = np.zeros([5, 6])

# np.reshape
a = np.arange(6).reshape([3, 2])
"""
array([[0, 1],
       [2, 3],
       [4, 5]])
"""

# np.full: fill a tensor with a certain value
np.full((2, 2), 10)
"""
array([[10, 10],
       [10, 10]])
"""

# np.sum
# Calculate second column of a matrix
MATRIX = np.arange(0, 9).reshape([3, 3])
result = np.sum(MATRIX[:, 1])

# np.matmul

# np.dot

# MATRIX_A @ MATRIX_B

#
