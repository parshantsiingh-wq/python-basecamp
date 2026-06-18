# write a program in which have one list and print only number not string and number should be greater


list=[1,2,3,4,5,6,7,8,9,"parshant", "aman ", "singh"]
found=False
for item in list:
    if type(item)==int:
        if item>=6:
            print("the item is :", item)
            found=True
if not found:
    print("sorry, your list has not interger item greater than and equal to 6")
