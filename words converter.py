num = int(input("Enter the number:"))
rcv = 0
cnt = num
while cnt > 0:
    digit = cnt % 10
    rcv = rcv* 10 + digit
    cnt//= 10
    if digit == 0:
        print("zero",end="")
    elif digit == 1:
          print("one",end="")
    elif digit == 2:
          print("two",end="")
    elif digit == 3:
        print("three",end="")
    elif digit == 4:
        print("four",end="")
    elif digit == 5:
        print("five",end="")
    elif digit == 6:
       print("six",end="")
    elif digit == 7:
        print("seven",end="")
    elif digit == 8:
        print("eight",end="")
    elif digit == 9:
        print("nine",end="")
        rcv //= 10