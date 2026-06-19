# use a list when you want to store multiple values in a single variable
# A list is mutable, which means its elements can be changed
number=["parshant", "singh", "aman" ,"pakisthan", 5, 78.6]
print(number)
print(len(number))
print(type(number))

# Access a specific element using its index
print(number[5])
# this will raise an IndexError because the index is out of range

#  list slicing
print(number[::])
print(number[:6:])    # by default, the step value is 1
print(number[0::])
print(number[2:6:])
print(number[2:5:2])
print(number[1:6:2])
print(number[::-1])
print(number[-5:-1:])
print(number[-5:-1:-1])   # Returns an empty list because the start, stop, and step values are incompatible
print(number[-1:-5:-1])
print(number[6:3:-1])
print(number[3:6:-1])   # its print empty list because of contradiction
print(number[5:6:-2])
print(number[-2:-6:-2])
print(number[-6:-2:-2])    # its print empty list because of contradiction
print(number)
a=[2,4,6,5,7,9,4,3,47,9]
print(a.sort())
print(a)
print(a.reverse())
print(a)
a.reverse()
print(a)
print(max(a))
print(min(a))
print(a.append(5))
print(a.insert(2,99))
print(a)
print(a.remove(5))
print(a)
print(a.pop())
print(a)
a[2]=5
print(a)
print(a)


# TUPLE
# A tuple is immutable
print("tuple is : \n")
T=(5,6,"PARSHANT")
print(T)
print(len(T))
print(type(T))
t=(1)  # it's not representation of tuple
print(type(t))
p=(1,)
print(type(p))



















