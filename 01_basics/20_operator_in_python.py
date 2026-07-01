# operators in python
# 1] arithmatic operators
# 2] assignment operators
# 3] comparision oprators
# 4] logical operators
# 5] identity operators
# 6] membership operator
# 7] bitwise operators


# arithmatic operators
print("arithmatic operator\n")
print("5+6 is:",5+6)
print("5-6 is:",5-6)
print("5*6 is:",5*6)
print("5/6 is:",5/6)
print("5**6 is:",5**6)
print("5//6 is:",5//6)
print("5%6 is:",5%6)

# assignment operators
print("\nassignment operators\n")
x=8
print(x)
x+=3
print(x)
x-=6
print(x)
x*=2
print(x)
x/=5
print(x)

# comparision operators
print("\ncomparision operators\n")
i=5
print(i==5)
print(i<5)
print(i>=5)
print(i!=7)

# logical operators
print("\nlogical operators\n")
a=True
b=False
print(a and b)
print(a or b)

# identity operators
print("\nidentity operator\n")
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)      # True
print(a is c)      # False

print(a is not c)      # True

# membership operators
print("\nmembership operator\n")
v=[3,5,6,7,8,9,0]
print(6 in v)
print(6 not in v)

print("\nbitwise operator\n")
# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11
print(0 & 1)
print(0 | 1)

print(1 & 2)
print(1 | 2)




