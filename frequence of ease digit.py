num=int(input("enter the number: "))

count0 = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
while num > 0:
    digit= num % 10
    if digit == 0:
        count0+=1
    elif  digit ==1:
        count1 +=1
    elif  digit ==2:
        count2+=1
    elif  digit ==3:
        count3+=1 
    elif  digit ==4:
        count4+=1
    elif  digit ==5:
        count5+=1
    elif  digit ==6:
        count6+=1 
    elif  digit ==7:
        count7+=1
    elif  digit ==8:
        count8+=1
    elif  digit ==9:
        count9+=1 
    num = num // 10
    if count0 > 0:
        print( "0:", count0)
    if count1 > 0:
        print( "1:", count1 )
    if count2 > 0:
        print( "2:", count2)
    if count3 > 0:
        print( "3:", count3)  
    if count4 > 0:
        print( "4:", count4)  
    if count5 > 0:
        print( "5:", count5)  
    if count6 > 0:
        print( "6:", count6)  
    if count7 > 0:
        print( "7:", count7)  
    if count8 > 0:
        print( "8:", count8)  
    if count9 > 0:
        print( "9:", count9)  
     
        
          
       

