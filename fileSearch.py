"""
Program to search for and return
data in a file based on keywords.

"""

import os
import oschmod
import pandas as pd
import csv

tagDict = {}

##File names for files of interest
numFile = int( input('Enter number of files: ') )


fileNames = [ input('Enter File Name: ') for i in range(numFile)]


##Change the working directory to the location files are saved
path = input('Enter directory of notepad files: ')
os.chdir(path)

loc = os.getcwd()

##reading the PI Tags for each substation provided.
for file in fileNames:
    with open( file, mode = 'r', newline = '' ) as f:
        reader = csv.reader(f)
        tags = [ row[0] for row in reader ]

        tagDict[file[:-4]] = tags


##May need to change directory again to read the files
fileDir  = input()
os.chdir(fileDir)
newloc = os.getcwd()

for sub in tagDict.keys():
    
    with open("BooneTest.csv", mode = 'r', newline = '') as f2:
        reader2 = csv.reader(f2)
        row = next(reader2) ## Getting rid of the header
        for row in reader2:
            if row[0] in tagDict[sub]:
                print('row stuff in second open: ', row)
                file = os.path.join(newloc, "Tag_"+ row[0] +".dat")
                with open(file, mode = 'a+', encoding = 'utf-8') as g:
                    assert os.path.isfile(file)
                    oschmod.set_mode( os.path.basename(file), 'a+rwx' )
                    writer = csv.writer(g)
                    g.writelines( txt + ' ' for txt in row )
                    g.write('\n')
            else:
                print(sub + ' not found')
                break ##go to the next item in list of dict keys
       
print("\n\n Successfully Completed")
