# no of guesses:9
# print no of guess left
# no of guess he took to finsih
# game over

n=19
i=0
print("hey you have 9 no of guesses")
while i<9:
    i+=1
    num=int(input("please,enter your number: \n"))
    if num==n:
        print("great, you took no of guesse to finsih this:",i)
        break
    else:
        diff=n-num
        var=max(num,n)
        if var==num:
            print("item is a backside")

        else:
            print()
            print("item is a frontside")
            print()
        print("no of guesses are left:",9-i)
        if i==9:
           print("Game over")


