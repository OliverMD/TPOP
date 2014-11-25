import math
def isPal(string):
    a = len(string)
    return string == string[::-1]

def getMaxPal(maxnum):
    maxPal = 0
    for i in range(90000009, maxnum):
        if isPal(str(i)):
            maxPal = max(maxPal, i)
    print "Found palindrome:", maxPal
    return maxPal
def factorPal(num):
    for i in range(0,98):
        if num %(99 - i) == 0:
            for j in range(0,98):
                if num % (99-j) == 0:
                    for k in range(0,98):
                        if num % (99-k) == 0:
                            for l in range(0,98):
                                if num % (99-l) == 0:
                                    if (99-i) * (99-j) * (99-k) * (99-l) == num:
                                        return (99-i, 99-j, 99-k, 99-l)
    print "Factors of:", num, "not found, continuing down!"
    #return factorPal(nextPalDown(num))
    return False

def nextPalDown(num):
    if len(str(num)) % 2 == 0:
        tens = math.floor(math.log10(num))
        power = (tens-1)/2
        a = num - (11 * (10**power))
        i = 1
        while isPal(str(int(a))) == False:
            power = ((tens-1)/2)-i
            a = num - (11 * (10**power))
            i +=1
    else:
        tens = math.floor(math.log10(num))
        a = num - (10**(tens/2))
        if isPal(str(int(a))) == False:
            a = a -1
    return int(a)

a = nextPalDown(getMaxPal(99**4))

#Used loop to avoid hitting recursion limit.

while True:
    a = nextPalDown(a)
    if factorPal(a) != False:
        print factorPal(a)
        break
