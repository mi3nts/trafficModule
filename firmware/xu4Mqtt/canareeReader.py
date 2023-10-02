#
import serial
import datetime
from mintsXU4 import mintsSensorReader as mSR
from mintsXU4 import mintsDefinitions as mD
import sys

dataFolder  = mD.dataFolder
ipsPorts    = mD.canareePorts
baudRate    = 115200

def main(portNum):
    if(len(ipsPorts)>0):
        ser = serial.Serial(
        port= ipsPorts[portNum],\
        baudrate=baudRate,\
        parity  =serial.PARITY_NONE,\
        stopbits=serial.STOPBITS_ONE,\
        bytesize=serial.EIGHTBITS,\
        timeout=0)

        print(" ")
        print("Connected to: " + ser.portstr)
        print(" ")

        #this will store the line
        line = []

        while True:
            try:
                for c in ser.read():
#                   print(chr(c))
                    line.append(chr(c))
                    if chr(c) == '\n':
                        dataString     = (''.join(line))
                        dataStringPost = dataString.replace('\n', '')
                        print("================------------------------================")
                        # print(dataStringPost)
                        mSR.IPS7100WriteV2(dataStringPost,datetime.datetime.now())
                        line = []
                        break
            except OSError as e:
                print ("Error: %s - %s." % (e.filename, e.strerror))
                print("Canaree Not Connected: Check connection")
        ser.close()

if __name__ == "__main__":
    print("=============")
    print("    MINTS    ")
    print("=============")
    portNum = int(sys.argv[1])
    print("Number of IPS7100 devices: {0}".format(len(ipsPorts)))
    print("Monitoring IPS7100 on port: {0}".format(ipsPorts[portNum]) + " with baudrate " + str(baudRate))
    main(portNum) 