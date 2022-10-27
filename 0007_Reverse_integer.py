# Constraints:

#     -231 <= x <= 231 - 1


def reverse(x):
    if x == 0:
        return 0
    y = abs(x)
    y = int(str(y)[::-1])
    if x < 0 and -y < -2**31 or x>0 and y>=2**31:
        return 0
    if x>0:
        return y
    else:
        return -y

testCases = [123,-123,120]
for num in testCases:
    print('test ',num,' :',reverse(num))