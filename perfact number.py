num=int(input("Enter the number:"))
sum=0
for i in range (1,num):
   #if num%10==0
   if num % i == 0:
    sum+= i
if sum == num:
    print("is perfact number")
else:
    print("is not a perfact number")
    
