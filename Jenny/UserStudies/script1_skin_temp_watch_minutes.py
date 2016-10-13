import os
import glob

personfolder = 'S11'

pathper = os.getcwd() +'/'+personfolder+'/'

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

total = 0

#Initial loop for one file
# Open file (day)
csvFile = open(pathper + '11November' + '/' + '2016-01-01_basis_metrics.csv',r)
column = "1"

lines = csvFile.readlines()
AverageArr = [None]*len(lines[0].split(',')
print (AverageArr)
for line in lines:
    #Skips empty lines
    if len(line) >0: 
        temparr = line.split(',')
        if temparr[0] != "datetime" and temparr[0] != ""
            varVal = varVal + temparr[column]
        
if notFound :
    finalstring = finalstring + line
    notFound = False
elif temparr[0] !="datetime" and temparr[0] != "":
    finalstring = finalstring + line


'''
for month in patharr:
    print("Current month: " + month)
    path = pathper + month
    
    finalstring = ""
    
    #count = 0
    notFound = True
    for filename in glob.glob(os.path.join(path, '*.csv')):
        file = open(filename,'r')
        lines = file.readlines()
        for line in lines:
            if len(line) >0:
                temparr = line.split(',')
                if notFound :
                    finalstring = finalstring + line
                    notFound = False
                elif temparr[0] !="datetime" and temparr[0] != "":
                    finalstring = finalstring + line
        #count += 1
        file.close()
        
        #os.remove(personfolder+'.csv')
        
        finalfile = open(personfolder+'.csv','w')
        finalfile.write(finalstring)
        finalfile.close()
        
        #pathtofinal = 'c:/Mikkel/JennyPython/S14Final.csv'
        finalfile = open(personfolder+'.csv','r')
        allLines = finalfile.readlines()
        count = 0
        finalSum = 0.0 
        loopCount = 0
        for line in allLines:
            if (loopCount == 0) :
                loopCount = 1 
                continue 
            temparr = line.split(',')
            if(len(temparr) > 0):
                if(temparr[1] != ""): #Column we look at (remember to count from 0)
                    count = count +1
                    #print (temparr[1])
                    finalSum = finalSum + float(temparr[1])
    averageF = finalSum / count
    averageC = (averageF -32.0) * (5.0/9.0)
    total = total + averageC 
    print ("Number of data points: " + str(count))
    print ("FinalSum of data points: " + str(finalSum))
    print ("Average in Fahrenheit: " + str(averageF))
    print ("Average in Celsius: " + str(averageC))
    print ("")
print ("total average: " + str(total / len(patharr)))
'''
