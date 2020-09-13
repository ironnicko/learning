import os
import numpy as np
import random
import matplotlib.pyplot as plt

os.rename('Lines.py', 'NumPy.py')

# 'dtype=' lets you decide the int8 or datatype. Remember, this isn't exactly like list, this one's better than list
a = np.array([[5, 151, 4], [4, 51, 1]], dtype='int16')
# .itemsize returns the item's size and .shape returns the co-ordinates. .ndim returns the dimention
print(a.itemsize, a.shape, a.ndim, end='\n')
# slicing is possible
print(a[-1::-1])
# Getting fancy here [start index:endindex:stepsize] basic slicing
print(a[0, 0::2])

# all zeroes matrix
b = np.zeros((2, 3))
print(b)

# Any other no.
print(np.full((2, 2), 99, dtype='int8'))

# any other number (full_number)

print(np.full_like(a, 5))

# Random decimal no.s

print(np.random.rand(4, 2))

# Random INT values

print(np.random.randint(4, 50, (2, 2)))  # the last tuple is for the size/shape

# Matrix

print(np.identity(5))

# Repeat
arr = np.array([[1, 2, 3]])
r1 = np.repeat(arr, 3, axis=0)
print(r1)

output = np.ones((5, 5))

z = np.zeros((3, 3))

output[1:-1, 1:-1] = z
print(output)

# Trignometric Values

a = np.sin([3, 3, 11, 31, 51, 31])

print(a)

# Matrix Calculation

a = np.ones((2, 3))
b = np.full((3, 2), 2)
print(np.matmul(a, b))  # matrix multiplication

c = np.identity(3)
print(np.linalg.det(c))  # det of matices

# Statistics

a = np.array([[1, 23, 132], [121, 1, 31]])
print(np.min(a, axis=0))
print(np.sum(a, axis=0))

# Reshape
before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(before)

after = before.reshape((2, 4))
print(after)

# Miscellaneous
# filedata = np.genfromtxt('t.txt', delimiter=',')
# filedata.astype('int32')

# os.system('clear')
