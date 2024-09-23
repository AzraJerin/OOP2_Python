# Python program to convert a list to string using the list comprehension and the join() method  
     
# Creating a list with some elements of int data type  
iterable = ["Python", "Convert", 11, "List", 12, "String", "Method"]  
    
# Converting to string using list comprehension  
string = " ".join ([str( elements ) for elements in iterable])  
  
# Printing the string  
print (string)   
print (type(string))  