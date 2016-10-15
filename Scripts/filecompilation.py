import os
import glob

personfolder = 'S20'

path = os.getcwd() +'/'+personfolder+'/'

#pathfolder = '11November'
#pathfolder = '12December'
#pathfolder = '01January'
#pathfolder = '02February'
#pathfolder = '03March'
#pathfolder = '04April'
pathfolder = '05May'
#pathfolder = '06June'
#pathfolder = '07July'

path = path + pathfolder

logstr = ""

finalstring = ""

#Number of hours missing for a day to be declared invalid, in minutes
dayHoursMis = 8*60
nightHoursMis = 2*60
#nightcount = 0

count = 0
for filename in glob.glob(os.path.join(path, '*.csv')):
    file = open(filename,'r')
    lines = file.readlines()
    for line in lines:
        if len(line) >0:
            temparr = line.split(',')
            if count == 0 :
                finalstring = finalstring + line
            elif temparr[0] !="datetime":
                finalstring = finalstring + line
    count += 1
    file.close()

finalfile = open(personfolder+'.csv','w')
finalfile.write(finalstring)
finalfile.close()

#pathtofinal = 'c:/Mikkel/JennyPython/S14Final.csv'
numMissLinNight = {}
numMissLinMorn = {}
numMissLinDay = {}
finalfile = open(personfolder+'.csv','r')
allLines = finalfile.readlines()
for line in allLines:
    temparr = line.split(',')
    if(len(temparr) > 0):
        if(temparr[1] == ""):
            #There is no data here
            arrdate = temparr[0].split(" ")
            hour = int(arrdate[1].split(":")[0])
            if( hour >= 7 and hour <= 23):
                if arrdate[0] in numMissLinDay:
                    numMissLinDay[arrdate[0]] = numMissLinDay[arrdate[0]] +1
                else:
                    numMissLinDay[arrdate[0]] = 1
            elif ( hour < 7) :
                if arrdate[0] in numMissLinMorn:
                    numMissLinMorn[arrdate[0]] = numMissLinMorn[arrdate[0]] +1
                else:
                    numMissLinMorn[arrdate[0]] = 1
            else:
                if arrdate[0] in numMissLinNight:
                    numMissLinNight[arrdate[0]] = numMissLinNight[arrdate[0]] +1
                else:
                    numMissLinNight[arrdate[0]] = 1
#file.close()
missdays = 0
#print (numMissLinDay)
logstr += str(numMissLinDay) + '\n'
for date, count in numMissLinDay.items():
    if count >= dayHoursMis:
        missdays += 1
#print ("Missing days ",missdays)
logstr += "Missing days " + str(missdays) + '\n'
#print (numMissLinNight)
logstr += str(numMissLinNight) + '\n'
#print (numMissLinMorn)
logstr += str(numMissLinMorn) + '\n'

numMissLinMornNight = {}

for date, count in numMissLinMorn.items():
    arrdate = date.split('-')
    day = int(arrdate[2])-1
    if day in numMissLinMornNight:
        numMissLinMornNight[day] = numMissLinMornNight[day] +count
    else:
        numMissLinMornNight[day] = count
#print (numMissLinMornNight)
logstr += str(numMissLinMornNight) + '\n'

for date, count in numMissLinNight.items():
    arrdate = date.split('-')
    day = int(arrdate[2])
    if day in numMissLinMornNight:
        numMissLinMornNight[day] = numMissLinMornNight[day] +count
    else:
        numMissLinMornNight[day] = count
#print (numMissLinMornNight)
logstr += str(numMissLinMornNight) + '\n'

missnight = 0
for date, count in numMissLinMornNight.items():
    if count >= nightHoursMis:
        missnight += 1
#print("Missing night",missnight)
logstr += "Missing night " + str(missnight)

logfile = open(personfolder+'/' +pathfolder + '.txt','w')
print (logstr)
logfile.write(logstr)
logfile.close()

