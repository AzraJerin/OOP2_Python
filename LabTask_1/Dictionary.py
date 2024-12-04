# Initial dictionary
employee = {
    "name": "A",
    "age": 40,
    "type": {"developer": ["iOS", "android"]},
    "permanent": True,
    "Salary": 30000,
    100: (1, 2, 3),
    4.5: {5, 6, 7, 1}
}

# 1. Print the length and type of the dictionary
print("Length of the dictionary:", len(employee))
print("Type of the dictionary:", type(employee))

# 2. Access the key "type" -> "developer"
developer_types = employee["type"]["developer"]
print("Developer types:", developer_types)

# 3. Change the value of "permanent" to False
employee["permanent"] = False
print("Updated dictionary:", employee)

# 4. Add a new key "gender" with the value "male"
employee["gender"] = "male"
print("Dictionary after adding 'gender':", employee)

# 5. Remove the "age" key from the dictionary
employee.pop("age", None)  # Using None as a default to avoid KeyError if "age" is not present
print("Dictionary after removing 'age':", employee)

# 6. Use keys(), values(), and items()
print("Keys:", employee.keys())
print("Values:", employee.values())
print("Items:", employee.items())

# 7. Iterate over the dictionary using a loop
print("Iterating over the dictionary:")
for key, value in employee.items():
    print(f"{key}: {value}")
