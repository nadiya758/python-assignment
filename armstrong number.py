start =int(input("Enter the start  number:"))
end =int (input ("Enter the end number:"))

for i in range (start, end +1 ):
    digits = len(str (i))

    sum = 0
    temp = i

    while temp>0 :
        digit = temp % 10
        sum += digit**digit
        temp = temp // 10
    if sum == i:
        print(i)

