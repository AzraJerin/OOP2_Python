# Importing the random module  
import random  
  
# Creating a string  
my_string = "Hello, World!"  
print("Original string:", my_string)  
  
# Convert the string to a list  
my_list = list(my_string)  
# ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']  
  
# Shuffle the list  
random.shuffle(my_list)  
# ['H', ',', 'o', 'e', 'l', 'W', 'l', '!', 'd', 'r', 'o', ' ', 'l']  
  
# Convert the list back to a string  
shuffled_string = ''.join(my_list)  
  
# Print the shuffled string  
print("Shuffled String:", shuffled_string)  