import os
import sys
import shutil
import datetime
from mintsXU4 import mintsSensorReader as mSR
from mintsXU4 import mintsDefinitions as mD

dataFolder    = mD.dataFolder
dataFolderCC  = mD.dataFolderCC
dataFolderRef = mD.dataFolderReference
macAddress    = mD.macAddress


def main():
    dateStart      = datetime.date(2016, 12, 6)
    deleteDaysBack = 30
    dateEnd =  datetime.date.today() -  datetime.timedelta(deleteDaysBack)

    deleteDays = [dateStart + datetime.timedelta(days=x) for x in range((dateEnd-dateStart).days + 1)]

    for deleteDate in deleteDays:
        try:
            dirPath = os.path.normpath(getDeletePath(deleteDate))
            print("Deleting: "+ dirPath)
            if os.path.exists(dirPath):
                shutil.rmtree(dirPath)

        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))
        

    for deleteDate in deleteDays:
        try:
            dirPath = os.path.normpath(getDeletePathRef(deleteDate))
            print("Deleting: "+ dirPath)
            if os.path.exists(dirPath):
                shutil.rmtree(dirPath)

        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))

    for deleteDate in deleteDays:
        try:
            dirPath = os.path.normpath(getDeletePathCC(deleteDate))
            print("Deleting: "+ dirPath)
            if os.path.exists(dirPath):
                shutil.rmtree(dirPath)

        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))
            
            
            
def getDeletePath(deleteDate):
    deletePath = dataFolder+"/"+macAddress+"/"+str(deleteDate.year).zfill(4)  + \
    "/" + str(deleteDate.month).zfill(2)+ "/"+str(deleteDate.day).zfill(2)
    return deletePath;
  
def getDeletePathCC(deleteDate):
    deletePath = dataFolderCC+"/"+macAddress+"/"+str(deleteDate.year).zfill(4)  + \
    "/" + str(deleteDate.month).zfill(2)+ "/"+str(deleteDate.day).zfill(2)
    return deletePath;  

def getDeletePathRef(deleteDate):
    deletePath = dataFolderRef+"/"+macAddress+"/"+str(deleteDate.year).zfill(4)  + \
    "/" + str(deleteDate.month).zfill(2)+ "/"+str(deleteDate.day).zfill(2)
    return deletePath;


if __name__ == '__main__':
  main()