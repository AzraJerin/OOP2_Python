#printing
print("Hello World! I Don't Give a Bug")

# sample comment 
# This is Python Comment
name = "geeksforgeeks"
print(name) 

# An integer assignment
age = 45
# A floating point
salary = 1456.8
# A string
name = "John"
print(age)
print(salary)
print(name)

x = "Hello World" # string
x = 50  # integer
x = 60.5  # float
x = 3j  # complex
x = ["geeks", "for", "geeks"]  # list 
x = ("geeks", "for", "geeks")  # tuple
x = {"name": "Suraj", "age": 24} # dict
x = {"geeks", "for", "geeks"} # set
x = True  # bool
x = b"Geeks" # binary

# Python program show input and Output
val = input("Enter your value: ") 
print(val) 

a = 9
b = 4
add = a + b 
sub = a - b 
mul = a * b 
mod = a % b 
p = a ** b 
print(add) 
print(sub) 
print(mul) 
print(mod) 
print(p)

a = True
b = False
print(a and b) 
print(a or b) 
print(not a)

a = 10
b = 4
print(a & b) 
print(a | b) 
print(~a) 
print(a ^ b) 
print(a >> 2) 
print(a << 2) 

a = 10
b = a 
print(b) 
b += a 
print(b) 
b -= a 
print(b) 
b *= a 
print(b) 
b <<= a 
print(b)
i = 20
if (i < 15): 
    print("i is smaller than 15") 
    print("i'm in if Block") 
else: 
    print("i is greater than 15") 
    print("i'm in else Block") 
print("i'm not in if and not in else Block") 

i = 20
if (i == 10): 
    print("i is 10") 
elif (i == 15): 
    print("i is 15") 
elif (i == 20): 
    print("i is 20") 
else: 
    print("i is not present") 
for i in range(0, 10, 2): 
    print(i) 

    count = 0
while (count < 3): 
    count = count + 1
    print("Hello Geek")

    def evenOdd():
      if(x % 2 == 0):
        print("even")
      else:
        print("odd")


# Driver code to call the function
evenOdd(2)
evenOdd(3)