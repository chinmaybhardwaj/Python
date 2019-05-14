import numpy as np

#
# Different usage of numpy array
#

# Creating simple ndArray
arr = np.array([1,2,3,4,5,6])
print(arr)

# Array using arange funcation
arr = np.arange(1,10,2)
print(arr)
print('Type:',arr.dtype)

# Array using arange funcation
arr = np.linspace(1,12,6)
print(arr)


print('\n\nSize:',arr.size)
print('Shape:',arr.shape)
print('Type:',arr.dtype)

arr = arr.reshape(3,2)
print('\n\nArray:',arr)
print('Size:',arr.size)
print('Shape:',arr.shape)
print('Type:',arr.dtype)

# How much byte does element take
print('\n\nByte:', arr.itemsize)


#Compare each element with a value
print('\n\n Comapring Elements:\n',arr < 4)


# Creating Zeros Array
arr = np.zeros((4,5))
print('\n\n Array with each element = 0:\n',arr)
print('Type:',arr.dtype)


# Creating Ones Array
arr = np.ones((7,9))
print('\n\n Array with each element = 1:\n',arr)
print('Type:',arr.dtype)


# Creating 1-D Ones Array
arr = np.ones(8)
print('\n\n 1-D Array with each element = 1:\n',arr)


# Passing Datatype of array
arr = np.array([2,3,4], dtype=np.int16)
print('\n\n Array:\n',arr)
print('Type:',arr.dtype)
print('Byte:', arr.itemsize)


# Creating Random array between 0 to 1
arr = np.random.random((2,3)) # Random between 0 to 1
print('\n\n Random Array:\n',arr)
print('Type:',arr.dtype)
print('Byte:', arr.itemsize)
np.set_printoptions(precision=2, suppress=True)
print('Array after printoptions:\n', arr)

# Creating Random array
arr = np.random.randint(0,10,5) # Random between 0 to 10. Array length = 5
print('\n\n Random Array:\n',arr)


# Mathematical operations on array
print('\n\n Sum of Array:\n',arr.sum())
print('Min Value of Array:\n',arr.min())
print('Max Value of Array:\n',arr.max())
print('Mean Value of Array:\n',arr.mean())
print('Variance of Array:\n',arr.var())
print('Standard Deviation of Array:\n',arr.std())

arr = np.random.randint(0,10,6)
arr = arr.reshape([3,2])
print('\n\nArray:\n',arr)
# Mathematical operations on row or comlumn only. Not on entire array
print('\n\nRow wise Sum:\n',arr.sum(axis=1)) # horizontal sum
print('Column wise Sum:\n',arr.sum(axis=0)) # vertical sum
print('Min Value horizontal:\n',arr.min(axis=1)) # horizontal
print('Standard Deviation vertical:\n',arr.std(axis=0)) # vertical



# Load Text files in array
# data = np.loadtxt('data.txt', delimiter=',', skiprows=1)

# Random Shuffle Array
arr = np.arange(10)
print('\n\nArray:\n',arr)
np.random.shuffle(arr)
print('\n\n Shuffled Array:\n',arr)


# Random Choice Array
choice = np.random.choice(arr)
print('\n\nRandom Choice:\n',choice)
