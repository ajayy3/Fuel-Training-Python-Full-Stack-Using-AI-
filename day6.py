# import numpy as np
# z=np.array([3,1,2])

# print(np.sort(z))
# print(np.sort(z)[::-1])
#---------------------------------------------------------------------------------------------------------
# 1 Question solution

#create an array of number 1 to 20 and print only the even number 
# import numpy as np
# numbers = np.arange(1, 21)
# even_numbers = numbers[numbers % 2 == 0]
# print(even_numbers)
#---------------------------------------------------------------------------------------------------------
# 2 Question solution

#Create a 3*3 matrix using arrange and reshape , then print row sums and column sums of the matrix
# import numpy as np
# matrix = np.arange(1, 10).reshape(3, 3)
# print("Matrix:")
# print(matrix)
# print("Row sums:")
# print(np.sum(matrix, axis=1))
# print("Column sums:")
# print(np.sum(matrix, axis=0))
#---------------------------------------------------------------------------------------------------------
# 3 Question solution

#convert the temperature [0,20,37,100] from celsius to fahrenheit in one line
# import numpy as np
# fahrenheit = np.array([0, 20, 37, 100]) * 9/5 + 32
# print(fahrenheit)
#---------------------------------------------------------------------------------------------------------
# 4 Question solution

#apply 10% discount to the price above 500 in an array using np.where
# import numpy as np
# prices = np.array([400, 600, 300, 700])
# discounted_prices = np.where(prices > 500, prices * 0.9, prices)
# print(discounted_prices)
#---------------------------------------------------------------------------------------------------------
# 5 Question solution

#generate 10 random integers from 1 to 100(seed7) and print mean,max,min and the sorted array
# import numpy as np
# np.random.seed(7)
# random_integers = np.random.randint(1, 101, 10)
# print("Random Integers:", random_integers)
# print("Mean:", np.mean(random_integers))
# print("Max:", np.max(random_integers))
# print("Min:", np.min(random_integers))
# print("Sorted Array:", np.sort(random_integers))
#---------------------------------------------------------------------------------------------------------
# 6 Question solution

#normzlise an array using (x-min)/(max-min) formula
# import numpy as np    
# normalized_array = (random_integers - np.min(random_integers)) / (np.max(random_integers) - np.min(random_integers) )
# print("Normalized Array:", normalized_array)
#---------------------------------------------------------------------------------------------------------
# 7 Question solution

# find the mean and standard deviation of an array of marks
# import numpy as np
# marks = np.array([85, 90, 78, 92, 88])
# mean_marks = np.mean(marks)
# std_dev_marks = np.std(marks)
# print("Mean:", mean_marks)
# print("Standard Deviation:", std_dev_marks)
#---------------------------------------------------------------------------------------------------------
# 8 Question solution

#replace all negative values in an array with 0
# import numpy as np
# array = np.array([-1, 2, -3, 4, -5])
# array[array < 0] = 0
# print(array)
#---------------------------------------------------------------------------------------------------------
# 9 Question solution
#create a 4*4 identity matrix and multiply it by 5

# import numpy as np
# identity_matrix = np.eye(4)
# result = identity_matrix * 5
# print(result)
#---------------------------------------------------------------------------------------------------------
# 10 Question solution
# comparethe time taken by a list and a numpy array to add 1,000,000 numbers
# import numpy as np
# import time  

#---------------------------------------------------------------------------------------------------------
