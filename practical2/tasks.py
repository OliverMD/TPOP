import math
def QuestionOne(a,b,c):
    def max(x,y):
        if x > y:
            return x
        else:
            return y
    return max(max(a,b),c)
def QuestionOneShow():
    assert QuestionOne(0,1,2) == 2
    assert QuestionOne(2,1,0) == 2
    assert QuestionOne(1,2,0) == 2
    assert QuestionOne(5,5,-7) == 5
    a = int(raw_input("Enter First Nummber: "))
    b = int(raw_input("Enter Second Number: "))
    c = int(raw_input("Enter Third Number: "))
    print "The greatest value entered is:", QuestionOne(a,b,c)
def QuestionTwo(hours,rate):
    hours = float(hours)
    rate = float(rate)
    total = 0.0
    overtime = 0.0
    if hours > 40.0:
        overtime = rate * 1.5 * (hours-40.0)
        hours = 40.0
    total = (hours * rate) + overtime
    return total, overtime
def QuestionTwoShow():
    hours = float(raw_input("Please enter number of hours: "))
    rate = float(raw_input("Please enter pay rate per hour: "))
    total, overtime = QuestionTwo(hours, rate)
    print "Total:", total, "Overtime amount:", overtime
def QuestionThree(speed, limit):
    if speed <= limit:
        return 0
    else:
        fine = 100 + ((speed-limit) * 5)
        if speed > 90:
            fine += 200
        return fine
def QuestionThreeShow():
    speed = float(raw_input("Enter speed clocked: "))
    limit = float(raw_input("Enter applicable limit: "))
    res = QuestionThree(speed, limit)
    if res == 0:
        print "The clocked speed was legal, no fine to pay"
    else:
        print "Fine to pay:", res
def LeapYear(year):
    year = math.floor(year)
    if (year%4 == 0) and ((not(year%100 == 0)) or (year%400 == 0)):
        return True
    return False
def DateValid(dateString):
    def dayValid(day,month, year):
        if day > 31 or day < 1:
            return False
        if month in [4,6,9,11] and day > 30:
            return False
        if LeapYear(year) and month == 2 and day >29:
            return False
        if month == 2 and day > 28:
            return False
        return True
        
    if len(dateString) != 10:
        return False
    vals = dateString.split("/")
    print vals
    day = int(vals[0])
    month = int(vals[1])
    year = int(vals[2])
    return dayValid(day,month,year)
