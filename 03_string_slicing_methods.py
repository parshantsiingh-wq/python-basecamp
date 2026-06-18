# string slicing and some string method
# slicing is used to access a specific part of string
var="parshant is a good boy"
# string can be long
print("the value of var is : ", var)
print("the type of var is: ",type(var))
print(len(var))

# string slicing
print(var[5])
print(var[-5])
print(var[0:6])    # [start: end: step] by default,step value is 1
print(var[12:18])
print(var[7:8:2])
print(var[7:15:2])
print(var[::])
print(var[:19:])
print(var[:19:2])
# when a negative step is used, the string is printed in reverse order
print(var[::-1])
# this does not work because the slice starts at index 7 and move toward index 12 with a step of -2
# a negative step moves backword, so no characters are returned
print(var[7:12:-2])
print(var[12:7:-2])
print(var[7:12:-2])
print(var[-1:-5:-2])
print(var[:78:])
print(var[::544])
print(var[-4:])
print(var[-14:-2:2])
print(var[-8:-2:])
print(var[15:19:-1])
print(var[::-2])

# methods in string that used
a="aman1"
print(var.isalnum())
print(a.isalnum())
print(var.isalpha())
print(a.isalpha())
print(var.endswith("boy"))
print(a.capitalize())
print(var.find("s"))
print(var.find("is"))
print(var.count("s"))
print(var.upper())
print(var.lower())
print(var.replace("a","k"))
print(var)


















