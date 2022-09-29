print('Welcome to Roman to integer number converter.\nThis converter is nOn cAsE sEnSiTiVe')

romanValues = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}

invInpErrTxt = 'Invalid input. Enter a Roman number. \n'


# for k in romanValues:
#     print(k, romanValues[k])

while True:
    numDict = []
    biggestTillNow = 0
    err = 0
    #s = input('Enter a Roman number you would like to convert: ')
    s = 'LVIII'

    #validating constrain: 1 <= s.length <= 15 
    if len(s) < 1:
        print('Input empty. Try again\n')
        continue
    elif len(s) > 15:
        print('Input too long. Maximum lenght of an input is 15 characters.\n ')
        continue
    
    #validating if input is a string
    try:
        s.upper()
    except:
        print(invInpErrTxt)
        continue

    i  = len(s) - 1

    while i >= 0:
        
        #validating if user input contains Roman number characters
        if s[i] not in romanValues:
            print(invInpErrTxt)
            break
        
        if len(numDict) > 0:
            x = romanValues[s[i]]
        
        numDict.append(x)
        i = i -1
    break
print(numDict)

        





