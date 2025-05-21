#sum of digits
num=int(input("enter the number:"))
sum = 0
while num!=0:
    degit=num%10
    sum+=degit
    num=num//10

print(" sum of degits",sum)