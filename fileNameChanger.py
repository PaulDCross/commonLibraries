import os

def rename(dirname, commonFileName, newEnd):
    for filename in os.listdir(dirname):
        #enter the bit you want removed here
        if filename.startswith(commonFileName):
            #the 15 is the amount of character in the previous statment
            os.rename(filename, commonFileName+newEnd)
