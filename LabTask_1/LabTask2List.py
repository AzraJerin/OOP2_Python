# Task 01
a = [1, 3, 5, 7, 4]

# 1) Access a[2], a[-2]
element_at_2 = a[2]
element_at_negative_2 = a[-2]
length_of_a = len(a)
type_of_a = type(a)
print(f"a[2]: {element_at_2}, a[-2]: {element_at_negative_2}")
print(f"Length of a: {length_of_a}, Type of a: {type_of_a}")

# 2) Change a[3] = 50, a[2:9]
a[3] = 50
# Since a only has 5 elements, a[2:9] will be a slice from index 2 to end
slice_a = a[2:9]
print(f"Updated list: {a}")
print(f"Slice a[2:9]: {slice_a}")

# 3) Add 100 in last index
a.append(100)
# Add 200 in index 2
a.insert(2, 200)
print(f"List after adding elements: {a}")

# 4) Remove last element
a.pop()
# Remove element on index 1
del a[1]
print(f"List after removing elements: {a}")

# 5) Join a new list [2, 4, 6] with a
new_list = [2, 4, 6]
a.extend(new_list)
print(f"List after joining: {a}")

# 6) Copy all values in a new list b
b = a.copy()
print(f"Copied list b: {b}")

# 7) Sort the elements of b
b.sort()
print(f"Sorted list b: {b}")

# 8) Print all the elements using loop and break if get 5
print("Elements of list b until 5:")
for elem in b:
    if elem == 5:
        break
    print(elem)

# 9) Find the largest number in a
largest_number = max(a)
print(f"Largest number in list a: {largest_number}")