print("*************** My Calculator ***************")
num1=float(input("Enter First Number: "))
num2=float(input("Enter Second Number: "))


print("1.Addition")
print("2.Substraction")
print("3.Multplication")
print("4.Division")
print("5.Floor Division")
print("6.Modulus")
print("7.Exponential")

choice=int(input("Enter Your Choice from 1 to 4!: "))

if choice==1:
    print("Addition of",num1,"and",num2,"is",num1+num2)

elif choice==2:
    print("Subtraction of",num1,"and",num2,"is",num1-num2)

elif choice==3:
    print("Multiplication of",num1,"and",num2,"is",num1*num2)

elif choice==4:
    if num2==0:
        print("Cannot Divide by Zero")
    else:
        print("Divison of",num1,"and",num2,"is",num1/num2)

elif choice==5:
    if num2==0:
        print("Cannot Divide by Zero")
    else:
        result=num1//num2
        print("Floor Division of",num1,"and",num2,"is",int(result))

elif choice==6:
    print("Modulus of",num1,"and",num2,"is",num1%num2)

elif choice==7:
    print("Exponential of",num1,"and",num2,"is",num1**num2)

else:
    print("Invalid Input!!!")

