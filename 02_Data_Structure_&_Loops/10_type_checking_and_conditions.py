items=[int,float,"parshant", 3,4,5,6,7,8,9,0]
print(items)
for item in items:
    if str(item).isnumeric() and item>=6:
        print("item:", item)
