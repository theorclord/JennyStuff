import os
import glob

personfolder = 'S11'

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

#total = 0
#averageCounter = 0

averageColumn = 1

firstLineAdd = True

finalString = ""


monthVal = 0.0
monthCounter = 0.0
path = pathper + patharr[0]#month
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
            # Adds the first line for the columns to have a header
            if firstLineAdd:
                finalString = finalString + line
                firstLineAdd = False
            temparr = line.split(',')
            #skips the first line in the file and empty lines
            if temparr[0] != "datetime" and temparr[0] != "":
                #first build final string
                finalString = finalString + line
                if temparr[averageColumn] != "":
                    #Construct the average
                    dayVal = dayVal + float(temparr[averageColumn])
                    dayCount = dayCount +1
            #end tempArr
    #end line
    dayAverage = dayVal/dayCount
    monthVal = monthVal + dayVal
    monthCounter = monthCounter + dayCount
    print("Average for " + filename + ": " + str(dayAverage))
monthAverage = monthVal/monthCounter
print("Average for " + patharr[0] + ": " + str(monthAverage))        
                    
                    
                
                



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


