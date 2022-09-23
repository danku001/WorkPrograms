"""
The purpose of this program is to read information
from a large (40GB) file and separate it based on Tags or
keywords

Save file in the same location as the documents  to read
Output files in the same location as script is in
"""


import os
import csv
import oschmod

#make sure you are in the same working directory as your file is in

loc = os.getcwd()

with open("tempValues.csv",
          mode = 'r', newline = '') as f:
    #use context manager to open large file
    reader = csv.reader(f)
    for row in reader :
        file = os.path.join(loc, 'Tag_' + row[0].replace(' ','') + '.txt')
        with open(file, mode = 'a+',
                  encoding = 'utf-8') as g:
            assert os.path.isfile(file)
            #explicitly setting permissions of file
            oschmod.set_mode( os.path.basename(file), 'a+rwx')
            writer = csv.writer(g)
            g.writelines( i + ' ' for i in row )
            g.write('\n')
