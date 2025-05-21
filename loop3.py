num=int(input("Enter the number:"))
reverse=0
x=num% 10
while num!=0:
    num//=10
    reverse=reverse*10 + x
print("number reverse",reverse)