# faulty calculator
num1=int(input("enter the value: \n"))
num2=int(input("enter the value: \n"))
operator= input("enter the operator: \n")

if operator=="+":
    if (num1==56):
        if(num2==9):
            print("the sum of two numebr: 77 ")
    else:
        print("the sum of two number:", num1+num2)
elif operator=="-":
    print("the difference of two number:", num1-num2)
elif operator=="*":
    if (num1==45):
        if(num2==3):
            print("the product of two number: 555 ")
    else:
        print("the product of two number:", num1 * num2)
elif operator=="/":
    if (num1 == 56):
        if (num2 == 6):
            print("the division of operator: 4")
    else:
        print("the division of operator:", num1/num2)
