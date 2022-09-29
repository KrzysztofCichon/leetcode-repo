def romanToInt(s):
    romanValues = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    numDict = []
    i  = len(s) - 1

    while i >= 0:
        if len(numDict) > 0 and romanValues[s[i]] < numDict[len(numDict)-1]:
            x = romanValues[s[i]] * -1
        else:
            x = romanValues[s[i]]
        numDict.append(x)
        i = i -1
    return sum(numDict)


xyz = input('Type Roman number: ')
print(romanToInt(xyz))