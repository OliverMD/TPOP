import math
def printImperial(mass):
    pounds = mass * 2.20462
    stone = math.floor(pounds / 14)
    pounds = pounds % 14
    print stone, "Stone,", pounds, "Pounds."
mass = float(raw_input("Enter mass in KG: "))
printImperial(mass)
