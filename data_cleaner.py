"""
Function to clean data from the file

"""

import os
import oschmod
import pandas as pd


def listFiles(PathToFile):
    """ Function to create a list of files
         in a directory

         Working directory needs to be the same as the
         location of all the files.
         
         Keyword arguments:
             PathToFile -> Raw string or string to directory


         Return:
             ret -> list of valid files in directory
    """
    os.chdir( PathToFile )
    tempFiles = os.listdir( path = os.getcwd() )
    ret = []
    
    for fi in tempFiles:
        if os.path.isfile( fi ):
            ret.append(fi)

    return ret


def dataCleaner(data):
    """ Function to clean all the data

        Working directory needs to be the same as the
        location of all the files.

        keyword arguements:
            data -> file name

        Return:
            *doesn't return anything*
    """
    ##Reading the data into a pandas dataframe
    df = pd.read_csv( data, header = None, low_memory = False )

    ##separating the data into different columns
    tempStr = '(\d{4})'
    df[['PItag','Value','Date']] = df[0].str.split( pat = tempStr,
                                                    n =1, expand = True,
                                                    regex = True )
    df.drop(columns = 0, inplace = True)

    ##Removing invalid text from data

    word_pat = "\[A-Za-z]*"
    date_pat = "^\d{1,2}[/]\d{1,2}[/]\d{4}\s*\d{1,2}\W\d{1,2}\W\d{2}\s*\w{2}"

    filt1 = df['Value'].str.strip()
    filt1 = filt1.str.contains( word_pat )

    filt2 = df['Date'].str.strip()
    filt2 = filt2.str.contains( date_pat )

    temp_df = df[~filt1]
    temp_df = temp_df[filt2]
       

    ##Converting to appropriate values
    temp_df['Value'] = pd.to_numeric( temp_df['Value'], downcast = 'integer' )
    temp_df['Date'] = pd.to_datetime( temp_df['Date'] ).dt.strftime( '%m/%d/%Y %H:%M:%S')
    temp_df['Date'] = pd.to_datetime( temp_df['Date'], format = '%m/%d/%Y %H:%M:%S' )

        
    return temp_df
    




fiLoc = input('Path to File Location: ')


##print( *( val for val in listFiles(fiLoc) ), sep ='\n' )

##Outputting  to pickle files
cleanFiles = input('File Location to store clean files: ')
##making sure the file permissions are open to reading and writting
oschmod.set_mode( cleanFiles, 'a+rwx' )

for val in listFiles( fiLoc ):
    clean_df = dataCleaner( val )
    clean_df.to_pickle( cleanFiles + '\\' + val[:-3] + "pkl")
