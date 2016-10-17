import os
import glob
import csv
import matplotlib.pyplot as plt
import numpy as np

personfolder = 'S12'

pathper = os.getcwd() +'\\'+personfolder+'\\'

#pathfolder = '11November'
#pathfolder = '12December'
#pathfolder = '01January'
#pathfolder = '02February'
#pathfolder = '03March'
#pathfolder = '04April'
#pathfolder = '05May'
#pathfolder = '06June'
#pathfolder = '07July'

patharr = []

patharr.append('11November')
patharr.append('12December')
patharr.append('01January')
patharr.append('02February')
patharr.append('03March')

averageColumn = 1

averageList = list()

#ConstVariables
PersonTotal = 0
personAverageCounter = 0
firstLineAdd = True
finalString = ""

for month in patharr:
    monthVal = 0.0
    monthCounter = 0.0
    path = pathper + month
    for filename in glob.glob(os.path.join(path,'*csv')):
        csvFile = open(filename,'r')

        dayVal = 0.0
        dayCount = 0.0

        #read all the lines in the file and create an average for the month
        #add the lines to the final file for use in graphs
        lines = csvFile.readlines()
        for line in lines:
            #Skips empty lines
            if len(line) >0:
                temparr = line.split(',')
                # Adds the first line for the columns to have a header
                if firstLineAdd:
                    finalString = finalString + line
                    firstLineAdd = False
                    print(temparr[averageColumn])
                #skips the first line in the file and empty lines
                if temparr[0] != "datetime" and temparr[0] != "":
                    #first build final string
                    finalString = finalString + line
                    if temparr[averageColumn] != "":
                        #Construct the average
                        if averageColumn == 1:
                            dayVal = dayVal + (float(temparr[averageColumn])-32)/1.8
                        else :
                            dayVal = dayVal + float(temparr[averageColumn])
                        dayCount = dayCount +1
                #end tempArr
        #end line
        if dayCount != 0:
            dayAverage = dayVal/dayCount
        else :
            dayAverage = 0
        #List for plot
        #averageList.append(dayVal)
        averageList.append(dayAverage)

        monthVal = monthVal + dayVal
        monthCounter = monthCounter + dayCount
        print("Average for day " + filename.split('\\')[len(filename.split('\\'))-1] + ": " + str(dayAverage))
    monthAverage = monthVal/monthCounter
    print("Average for " + month + ": " + str(monthAverage))
    PersonTotal = PersonTotal + monthAverage
    personAverageCounter = personAverageCounter + 1
personAverage = PersonTotal/personAverageCounter
print("Average for Person: " + str(personAverage))

#Writing final file for plots
finalFile = open("finalCSVfile.csv","w")
finalFile.write(finalString)
finalFile.close()

plotList = []

with open('finalCSVfile.csv', 'r') as f:
    reader = csv.reader(f)
    plotList = list(reader)


def mk_float(s):
    s = s.strip()
    return float(s) if s else 0

plotArr = np.array ( plotList)
print(plotArr[1:,averageColumn])
valueArr = np.array(list(map(mk_float,plotArr[1:,averageColumn])))
print(len(valueArr))
#plt.plot(range(0,len(valueArr)) ,valueArr)
#plt.show()

plt.plot(range(0,len(averageList)),averageList)
plt.show()
#String Handling the sleep
'''
# Final array not yet in use
AverageArr = [None] #*len(lines[0].split(','))
sleepDict = {}
column = 8
varVal = None
varCount = 0
for month in patharr:
    print("Current month: " + month)
    path = pathper + month
    #path = pathper + '01January'
    for filename in glob.glob(os.path.join(path,'*csv')):
        csvFile = open(filename,'r')
        
        # Loop for one file    
        # Open file (day)
        #csvFile = open(pathper + '01January' + '\\' + '2016-01-01_basis_metrics.csv','r')

        lines = csvFile.readlines()
        # loop for one column
        for line in lines:
            #Skips empty lines
            if len(line) >0:
                temparr = line.split(',')
                #for column in range(0,len(temparr)):
                    
                if temparr[0] != "datetime" and temparr[0] != "" and temparr[column] != "":
                    try:
                        tempVal = float(temparr[column])
                        if(varVal is None):
                            varVal = 0.0
                        varVal = varVal + tempVal
                    except Exception:
                        if(temparr[column] in sleepDict.keys()):
                            sleepDict[temparr[column]] = sleepDict[temparr[column]] +1
                        else:
                            sleepDict[temparr[column]] = 1
                        #Handel strings
                        #if(varVal is None):
                        #    varVal = ""
                        #varVal = temparr[column]
                    varCount = varCount +1
    #print(varVal)
    #print(varCount)
print(sleepDict)
print(varCount)
'''
