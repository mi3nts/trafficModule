
#!/usr/bin/python

import sys
import yaml
import os

print()
print("MINTS")
print()


from mintsXU4 import mintsSensorReader as mSR
from mintsXU4 import mintsDefinitions  as mD

nodeID         = mD.nodeID
dataFolder     = mD.dataFolder

airMarID       = mD.airMarID
dataFolderRef  = mD.dataFolderReference
dataFolderRaw  = mD.dataFolder


print("Data Folder: " + dataFolder)
print("Data Folder Raw: " + dataFolderRaw)
print("Data Folder Ref: " + dataFolderRef)

sysStr = 'rsync -avzrtu -e "ssh" ' +  "--include='*2023_03_*.csv' --include='*/' --exclude='*' mints@10.247.238.16:Downloads/reference/" + airMarID + " " + dataFolderRef
print(sysStr)
os.system(sysStr)
