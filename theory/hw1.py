def gcd(a,b):
    #gdc(int,int) -> int
    #Recursive implementation of GCD
    if a > b:
        c = a
        a = b
        b = c
    def internal(a,b):
        if a % b == 0:
            return b
        return internal(b,a%b)
    return internal(a,b)

def altGcd(a,b):
    #altGcd(int,int) -> int
    #A more literal interpretation of
    #the algorithm in the work sheet.
    while True:
        r = a % b
        if r == 0:
            return b
        a = b
        b = r
        
def divide(a,b):
    #divide(int,int) -> (quotient int, remainder int)
    #Divides a by b and returns quotient and remainder.

    #performed 200,000 divisions of 60034 by 234 in 2.947s
    #compared with 0.014s for the normal python divide.
    #Tested using cProfile from command line.
    q = 0
    while a - b >= 0:
        a = a - b
        q += 1
    return q, a
for i in range(0,200000):
    60034/234
