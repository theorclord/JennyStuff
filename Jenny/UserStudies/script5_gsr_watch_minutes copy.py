import os
import glob

personfolder = 'S20'

pathper = os.getcwd() +'/'+personfolder+'/'

pathfolder = '11November'
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

for month in patharr:
    print(month)
    path = pathper + month
    
    finalstring = ""
    
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
        finalfile = open(personfolder+'.csv','r')
        allLines = finalfile.readlines()
        count = 0
        for line in allLines:
            temparr = line.split(',')
            if(len(temparr) > 0):
                if(temparr[5] != ""): #Column we look at (remember to count from 0)
                    count = count +1
    print (count)