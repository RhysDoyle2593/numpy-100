#### 1. Import the numpy package under the name `np` (★☆☆)
import numpy as np

#### 2. Print the numpy version and the configuration (★☆☆)
#print(np.__version__)
#print(np.show_config())

#### 3. Create a null vector of size 10 (★☆☆)
#arr = np.zeros(10)
#print(arr)
#### 4. How to find the memory size of any array (★☆☆)
#print(arr.nbytes)

#### 5. How to get the documentation of the numpy add function from the command line? (★☆☆)
#???

#### 6. Create a null vector of size 10 but the fifth value which is 1 (★☆☆)
#z = np.zeros(10)
#z[4] = 1
#print(z)

#### 7. Create a vector with values ranging from 10 to 49 (★☆☆)
#j = np.arange(10, 50)
#print(j)
#### 8. Reverse a vector (first element becomes last) (★☆☆)
#k = np.flip(j)
#print(k)
#### 9. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)
# z = np.arange(9).reshape(3, 3)
# print(z)
# #### 10. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)
# z = np.array([1, 2, 0, 0, 4, 0])
# nonzero_indices = np.nonzero(z)
# print(nonzero_indices)
# #### 11. Create a 3x3 identity matrix (★☆☆)
# identity_matrix = np.eye(3)
# print(identity_matrix)
# #### 12. Create a 3x3x3 array with random values (★☆☆)
# random_array = np.random.random((3, 3, 3))
# print(random_array)
#### 13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)
random_array = np.random.random((10, 10))
min = np.min(random_array)
max = np.max(random_array)
print("Random array:\n", random_array)
print("Minimum value:", min)
print("Maximum value:", max)

#### 14. Create a random vector of size 30 and find the mean value (★☆☆)

#### 15. Create a 2d array with 1 on the border and 0 inside (★☆☆)

#### 16. How to add a border (filled with 0's) around an existing array? (★☆☆)