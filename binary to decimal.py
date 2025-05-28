
def Binary_to_decimal(Binary):
    decimal = 0
    num = 0
    while Binary > 0:
       digit = Binary % 10
       decimal += digit* (2**num)
       num += 1
       Binary = Binary // 10
    return decimal

