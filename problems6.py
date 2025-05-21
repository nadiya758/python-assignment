#1 comdition x>0 and y>0
#2 condition x<0 and y>0
#3 condition x<0 and y<0
#4 condition x>0 and y<0
#5 conditoin x==0 and y==0 (origin)
x=float (input("Enter the x coordinate :"))
y=float (input ("Enter the y coordinate :" ))
if x>0 and y>0:
    print("1st quedrant")
elif x<0 and y>0:
    print("2nd quedrant")
elif x<0 and y<0:
    print("3rd quedrant")
elif x>0 and y<0:
    print("4th quedrant")
 
elif x==0 and y==0:
    print("the quedrant is origin")
else:
    print ("invalid quedrant")
 




