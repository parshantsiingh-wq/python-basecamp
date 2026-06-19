# dictionary is like a key-value pairs
d={}
print(type(d))
di={"name" : "parshant", "roll_n0" : "27" ,"5" : 5, "list" : [5,6], "dic" : {"a":"apple", "b":"ball", "c":"cat"}}  # dictionart key can be number
print(di)
# A dictionary key is im-mutable
print(di["name"])
print(di["dic"]["b"])
di["eat"] = "simple_roti"
print(di)
di[420] = "NO"
print(di)
del di[420]
print(di)
del di["dic"]["c"]
print(di)
print(di.copy())
di["dic"]["c"]="cat"
print(di)
print(di.copy())
# where copy is used

d2=di
del d2["name"]
print(d2)
print(di)

print("\nhello\n")
d3=di.copy()
d3["name"]="parshant"
print(d3)
print(di)
print(d2)

print("dictionary is:\n")
d3=di.copy()
del di["eat"]
print(d3)
print(di)

print(d3.get("eat"))
print(d3)

d3.update({"name":"parshant"})
print(d3)

print(d3.keys())
print(d3.items())



