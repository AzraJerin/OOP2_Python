# Importing the random module  
import random  
  
# Generates a list of random numbers between 10 and 40  
random_list1 = random.sample(range(10, 40), 10)  
  
# Creating a sample list  
list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]  
  
# Generates a list of random numbers  
random_list2 = random.sample(list_, 5)  
  
# Printing Results  
print("List of random integers one:", random_list1)  
print("List of random integers two:", random_list2)  