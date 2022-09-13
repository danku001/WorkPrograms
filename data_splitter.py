"""
The purpose of this program is to read information
from a large (40GB) file and separate it based on Tags or
keywords
"""


import os
import csv


#make sure you are in the same working directory as your file is in
os.chdir("C:\\Users\\Bruce\\Desktop\\tempStuff")


with open("tempValues.csv", mode = 'r', newline = '') as f:
    #use context manager to open large file
    reader = csv.reader(f)
    for row in reader :
        with open('Tag_' + row[0] + '.csv', mode = 'a',
                  encoding = 'utf-8') as g:
            writer = csv.writer(g)            
            print(row)
            g.writelines( i + ' ' for i in row )
            g.write('\n')
