dict1={"name":"parshant", "roll_no":"27", "dept":"cse"}
#work an infinite time
print(dict1)
while(1):
    d=input("enter the value: \n")
    for keys,values in dict1.items():
        if d==keys:
            print("value is:", dict1[d])
            break

