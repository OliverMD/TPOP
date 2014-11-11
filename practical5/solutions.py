def min_Precipitation(fileName):
    """
    min_Precipitation(fileName string) -> float
    Returns the minimum rainfall ffrom all the years recorded
    in the file that fileName refers to in the local directory.
    """
    with open(fileName, 'r') as dataFile:
        dataFile.readline() #Ignore first line
        minFall = float(dataFile.readline()[:-2].split(',')[1]) #Set initial min
        for line in dataFile:
            data = line[:-2].split(',') #Split data, remove line delimiters.
            minFall = min(float(data[1]), minFall)
        return minFall

    
def max_Precipitation(fileName):
    """
    max_Precipitation(fileName string) -> float
    Returns the maximum rainfall ffrom all the years recorded
    in the file that fileName refers to in the local directory.
    """
    with open(fileName, 'r') as dataFile:
        dataFile.readline()
        maxFall = 0.0 #Seems reasonable to assume this is bottom limit.
        for line in dataFile:
            maxFall = max(float(line[:-2].split(',')[1]), maxFall)
        return maxFall
    
def average_Precipitation(fileName):
        """
    average_Precipitation(fileName string) -> float
    Returns the minimum average ffrom all the years recorded
    in the file that fileName refers to in the local directory.
    """
    with open(fileName, 'r') as dataFile:
        dataFile.readline()
        fallSum = 0.0
        cnt = 0.0
        for line in dataFile:
            fallSum += float(line[:-2].split(',')[1])
            cnt +=1
        avg = fallSum/cnt
        return avg

def collatePrecipitationFile(fileNames, outputFile):
    """
    collatePrecipitationFile(fileNames [string], outputFile string) -> None
    Collates the precicpation data from all the files in fileNames and adds
    this data to the appropriate year and saves it in outputFile.
    """
    data= []
    for name in fileNames[1:]:
        with open(name,'r') as dataFile:
            cnt = 0
            dataFile.readline()
            for line in dataFile:
                text = line[:-2].split(',')[1]
                try:
                    data[cnt].append(text)
                except IndexError:
                    data.append([text])
                cnt +=1
    print data
    with open(fileNames[0], 'r') as dataFile, open(outputFile, 'w') as outFile:
        dataFile.readline()#Ignore header
        for (line, dataLine)  in zip(dataFile, data):
            text = line[:-2] + ',' + (',').join(dataLine)+'\n'
            print text,
            outFile.write(text)
            
def collateData():
    """
    collateData(None) -> None
    Collates the data from aberporth_meteorlogical_data.txt and evaluates the total af, rain and sun for each year.
    It then saves it in aberporthCollated.csv with the data seperated by commas. It also provides a header at the
    start of the file identifying what data is in each column.
    """
    with open("aberporth_meteorological_data.txt", 'r') as dataFile, open('aberporthCollated.csv','w') as outFile:
        outFile.write("year,af,rain,sun\n")
        dataFile.readline()
        dataFile.readline()
        lastYearRead = ''
        newData = [0.0, 0.0, 0.0]
        for line in dataFile:
            if line[:4] == lastYearRead:
                temp = line[:-2].split(',')
                newData[0] += float(temp[4])
                newData[1] += float(temp[5])
                newData[2] += float(temp[6])
            else:
                if lastYearRead != '':
                    outFile.write(lastYearRead+",{0:.2f},{1:.2f},{2:.2f}\n".format(newData[0], newData[1], newData[2]))
                temp = line[:-2].split(',')
                newData = [float(temp[4]), float(temp[5]) , float(temp[6])]
            lastYearRead = line[:4]
collateData()
