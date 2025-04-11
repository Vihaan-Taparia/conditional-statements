num=(int(input("type an integer")))
if num > 0:
    print("That is a positive number")


    
num1=(int(input("type an integer")))
if num1 < 0:
    print("That is a negative number")





#profit or loss

cp=(int(input("Enter the cost price:")))
sp=(int(input("Enter the selling price:")))

if(sp>cp):
    print("That is a profit!")
    profit=sp-cp
    print(profit)

else:
    print("That is a loss")
    loss=cp-sp
    print(loss)



#greater than or lesser than
n1=(int(input("Write any number between 10 and 20:")))

if n1>15:
    print(n1,"is greater than 15")

else:
    print(n1,"is less than 15 ")


#odd even

n=int(input("Enter any number:"))

if n%2==0:
    print("That is an even number")

else:
    print('That is an odd number')