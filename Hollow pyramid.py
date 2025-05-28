rows=int(input("Enter the number of rows:"))
symbol=input("Enter the symbol:")
for i in range(1,rows + 1):
    print(""*(rows-i),end="")

if i==1:
    print(symbol)
elif i==rows:
    print(symbol*(2*i-1))
else:
    print(symbol+""*(2*(i-3)+ symbol))