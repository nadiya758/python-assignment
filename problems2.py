num1=int(input("Enter the 1st number:"))
num2=int(input("Enter the 2nd number:"))
operator=input("Enter the operator(+,-,*,/):")
if (operator=='/'):
    if num2==0 :
        print("cannot divide by zero")
    else:
         print("Ans",num1/num2)
elif operator=='*':
      print("Ans", num1*num2)
elif operator=='+':
     print("Ans",num1+num2)
else:
     print("Ans",num1-num2)
