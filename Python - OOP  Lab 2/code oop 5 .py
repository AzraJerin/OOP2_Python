P = int( input("Please enter value for P: "))  
Q = int( input("Please enter value for Q: "))  
   
# To swap the value of two variables  
# we will user third variable which is a temporary variable  
temp_1 = P  
P = Q  
Q = temp_1  
   
print ("The Value of P after swapping: ", P)    
 
   
# To Swap the values of two variables  
P, Q = Q, P  
   
print ("The Value of P after swapping: ", P)  
print ("The Value of Q after swapping: ", Q)  
 
  
   
# To Swap the values of two variables using XOR  
P = P ^ Q  
Q = P ^ Q  
P = P ^ Q  
   
print ("The Value of P after swapping: ", P)  
print ("The Value of Q after swapping: ", Q)  
 
 
   
# To Swap the values of two variables using Addition and subtraction operator  
P = P + Q    
Q = P - Q   
P = P - Q  
   
print ("The Value of P after swapping: ", P)  
print ("The Value of Q after swapping: ", Q)  