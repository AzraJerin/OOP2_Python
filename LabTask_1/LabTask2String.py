# Step 1: Declare variables
a = "hello"
b = "b2b2b2"
c = "3g3g"

# Step 2: Declare a new variable d and concatenate a, b, c
d = a + b + c
print("Concatenated String:", d)

# Step 3: Find the length of d and print d[:]
length_d = len(d)
print("Length of d:", length_d)
print("Substring d[:]:", d[:])

# Step 4: Check if "a2" is present in d
presence_check = "a2" in d
print("Is 'a2' present in d?", presence_check)

# Step 5: Perform the following string operations
print("Uppercase:", d.upper())
print("Lowercase:", d.lower())
print("Title case:", d.title())
print("Strip:", d.strip())
print("Is digit:", d.isdigit())
print("Find '3g':", d.find("3g"))
print("Capitalize:", d.capitalize())
print("Is alphanumeric:", d.isalnum())
print("Count 'b2':", d.count("b2"))
print("Split:", d.split())
print("Swapcase:", d.swapcase())
print("Left strip:", d.lstrip())
print("Replace 'hello' with 'python':", d.replace("hello", "python"))