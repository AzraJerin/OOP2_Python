def Fibo(Term):  
    values = []  
    First = 0  
    Second = 1  
    Next = First + Second  
    values.append(First)  
    values.append(Second)  
    for i in range(2,Term+1):  
        values.append(Next)  
        First = Second  
        Second = Next  
        Next = First + Second  
    return values  
Term = int(input())  
res=Fibo(Term)  
print(*res)  