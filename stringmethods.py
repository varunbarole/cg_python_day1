


name = "python programming"


print(name)

print(name.capitalize())

print(name.upper())

print(name)

print(name.lower())

print("Count of P:", name.count("p"))
# Original string is not getting modified.
print(name)

print(name.center(50))

print(name.center(50,"*"))

print(name.endswith("q"))

print(name.endswith("g"))

print(name.startswith("a"))

print(name.startswith("p"))

print("After replacing :", name.replace("python","scala"))

# If "tho" is existing .. it return the index number of t
print("check for availablity :", name.find("tho"))  # 2

# pe is not existing.. hence -1 is returned
print("check for availablity :", name.find("pe"))   

print(name.isalnum())

name = "  python  "
# remove space at the ends of the string
print(name.strip())

# remove space only at the left side
print(name.lstrip())

## remove space only at the right side
print(name.rstrip())


name = "python programming"
output = name.split(" ")
print(output)


name = "python programming"
output = name.split("p")
print(output)

# string length
print("Length of the string :",len(name))














