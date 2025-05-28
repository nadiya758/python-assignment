num=int(input("Enter the number:"))
while num >= 10:
    sum=0
    print(sum)
    while num > 0:
       # sum += num%10
       digit = num%10
       sum += digit
       num //= 10
    num = sum 
print("Digital roots is:",num)
