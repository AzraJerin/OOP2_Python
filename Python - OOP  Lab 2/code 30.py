n = int(input ("Enter the number you want to print: "))     
# Take input from user that how many numbers you want to print  
a = 0    
b = 1    
for i in range(0,n):  
    print(a, end = " ")             # a:0;    a:1;       a:2  
    c = a+b                     #c=0+1=1; c= 1+1=2;  c=1+2=3  
    a = b               #a=1    ; a=1;       a=2  
    b = c               #b=1    ; b=2;       b=3  
