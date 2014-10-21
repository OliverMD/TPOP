def printMetric(stones, pounds):
    #printMetric(stones,pounds) -> void
    #Prints weight in kg
    totalPounds = pounds + (stones*14)
    print "Mass:", 0.453592* totalPounds, "kg"
    return
x = float(raw_input("Enter Stones:"))
y = float(raw_input("Enter Pounds:"))

printMetric(x,y)
