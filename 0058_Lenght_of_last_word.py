# Constraints:

#     1 <= s.length <= 104
#     s consists of only English letters and spaces ' '.
#     There will be at least one word in s.


sInp = 'hello world'


def lengthOfLastWord(s):
    lst = s.split()
    return(len(lst[len(lst)-1]))


print('Testcase :',sInp,'\nResult: ',lengthOfLastWord(sInp))