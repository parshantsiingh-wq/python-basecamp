# when i take to decision then we will use if, else, elif

num1=56
num2=76

if num1>num2:
    print("num1 is greater")
if num1==num2:
    print("equal to number")
else:
    print("num2 is greater")

# same code write with elif statement

n1=98
n2=34

if(n1>n2):
    print("n1 is greater")
elif(n1==n2):
    print("equal number")
else:
    print("n2 is greater")

# work with list date structure using in keyword and not in keyword

list=[5,67,8,"parshant", "aman", "hello"]
print(6 not in list)
if "parshant" in list:
    print("it exist in list")
else:
    print("not exist in list")

# exercise
print("enter your value: \n")
n=int(input())
if n>18:
    print("yes you can drive")
elif n==18:
    print("we can think")
else:
    print(" sorry, you cannot drive")

