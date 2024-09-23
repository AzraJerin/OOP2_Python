# Python program to convert a list to string using the iteration method  
     
# Creating a list with all elements of string data type  
iterable = ["Python", "Convert", "List", "String", "Method"]  
  
# Creating a blank string  
string = ""   
  
# Starting a for loop to traverse through the list elements  
for element in iterable :   
    string = string + " " + element # Using " " as a separator for the elements of the string. However, it will add an extra space at the beginning of the string  
  
# printing the string  
print ( string )  