# Importing the random module  
import random  
  
# Creating a list  
rand_list = []   
  
# Using a for loop from 0 to 9  
for i in range(0, 10):  
  
    # Generates a random integer between 1 to 50   
    n = random.randint(1, 50)  
  
    # Appending the ramdom integer  
    rand_list.append(n)  
  
# Printing Results  
print("List of random integers:", rand_list)  