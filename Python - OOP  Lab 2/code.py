# create a program to generate a string with or without repeating the characters.  
import random  
import string  
print("Use of random.choice() method")  
def specific_string(length):  
     
    letters = string.ascii_lowercase # define the lower case string  
     # define the condition for random.choice() method  
    result = ''.join((random.choice(letters)) for x in range(length))  
    print(" Random generated string with repetition: ", result)  
  
specific_string(8) # define the length  
specific_string(10)  
  
  
print("") # print the space  
print("Use of random.sample() method")  
def WithoutRepeat(length):  
    letters = string.ascii_lowercase # define the specific string  
    # define the condition for random.sample() method  
    result1 = ''.join((random.sample(letters, length)))   
    print(" Random generated string without repetition: ", result1)  
  
WithoutRepeat(8) # define the length  
WithoutRepeat(10)   