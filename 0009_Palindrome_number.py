nums = [0, 10, -121, 121, 123321]

def isPalindrome(x):
    if x < 0:
        return(False)
    if str(x) == str(x)[::-1]:
        return(True)
    else:
        return(False)

for n in nums:
    print('Testcase:',n,'Returned:',isPalindrome(n))    