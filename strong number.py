#n=int(input("Enter the number:"))
#cnt=0
#sum=0

#digit=cnt%10
   #fact=1
   #while i<=digit:
      #fact*=i
     # i+=1
     # sum += fact
#cnt//=10
#if sum==n:
   #print("is a stong number")
#else:
 #  print("is  not a stong number")

num=int(input("Enter the number:"))
sum=0

while num> 0:
   digit = num % 10
   facto = 1
   while num>= 1:
      facto *= num
   sum += facto
   num //= 10
print("sum of factorial of digit is:",sum)
     


  


