list=["name", "singh", 5, "aman"]
print(list,"\n")

for item in list:
    print(item)

print("\nDisplay sublist of list: ")
new_list=[["parshnat", 1],["aman", 2],["raual", 3],["taran", 4]]
for item in new_list:
    print(item)

l=[["harry", 1],["varry", 2],["karrie", 3],["marie",4]]
print()
for element,value in l:
    print(element,"and value is:", value)

print()
p=[["harry", 1,2],["varry", 2,3],["karrie", 3,4],["marie",4,5]]
for element,value,coin in p:
    print(element,"and value is:", value, "and earn coins is :", coin)

print()
dict1=dict(l)
print(dict1)
# for element,value in dict1.items() gives no error becouse .items() returns key-value pairs
for element,value in dict1.items():
    print(element,"and value is:", value)
print()
for item in dict1:
    print(item)
