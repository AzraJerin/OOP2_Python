# Matrix multiplication using nested for loop  
# Initialize the value of the A and B matrix    
A = [[1,2,3],  
        [4,5,6],  
        [7 ,8,9]]  
B = [[0,0,1],  
       [0,1,0],  
       [1,0,0]]  
# Using nested list method with zip in Python    
multiResult = [[sum(a * b for a, b in zip(Arow, Bcol))     
                       for Bcol in zip(*B)]    
                                for Arow in A]    
# Printing multiplication result in the output    
print("The multiplication result of matrix A and B is: ")    
for res in multiResult:    
    print(res)    