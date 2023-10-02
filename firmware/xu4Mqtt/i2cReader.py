
#!/usr/bin/python
# ***************************************************************************
#   I2CPythonMints
#   ---------------------------------
#   Written by: Lakitha Omal Harindha Wijeratne
#   - for -
#   MINTS :  Multi-scale Integrated Sensing and Simulation
#     & 
#   TRECIS: Texas Research and Education Cyberinfrastructure Services
#
#   ---------------------------------
#   Date: July 7th, 2022
#   ---------------------------------
#   This module is written for generic implimentation of MINTS projects
#   --------------------------------------------------------------------------
#   https://github.com/mi3nts
#   https://trecis.cyberinfrastructure.org/
#   http://utdmints.info/
#  ***************************************************************************

import datetime
#import SI1132

from mintsXU4 import mintsSensorReader as mSR
from mintsXU4 import mintsDefinitions as mD

from mintsI2c.i2c_scd30 import SCD30
from mintsI2c.i2c_as7265x import AS7265X
from mintsI2c.i2c_bme280 import BME280
from mintsI2c.i2c_bme680 import BME680

import sys
import time
import os
import smbus2

debug  = False 

bus     = smbus2.SMBus(2)

scd30   = SCD30(bus,debug)
bme680  = BME680(bus,debug)
bme280  = BME280(bus,debug)

loopInterval = 10;

def main():

    scd30_valid    = scd30.initiate(30)
    bme280_valid   = bme280.initiate(30)
    bme680_valid   = bme680.initiate(30)
    
    startTime = time.time()
    while True:
        try:
            print("========================================================")
            print("======== SCD30 ========")
            if scd30_valid:
                dateTime = datetime.datetime.now()
                dataOut   = scd30.read()
                if dataOut is not None:
                    mSR.SCD30WriteI2c(dataOut,dateTime)
            print("=======================")
            time.sleep(2.5)

            print("========================================================")
            print("======= BME280 ========")
            if bme280_valid:
                dateTime = datetime.datetime.now()
                dataOut = bme280.read()
                if dataOut is not None:
                    mSR.BME280WriteI2c(dataOut,dateTime)
            print("=======================")
            time.sleep(2.5)            
            print("========================================================")            
            print("======= BME680 ========")
            if bme680_valid:
                dateTime = datetime.datetime.now()
                dataOut = bme680.read()
                if dataOut is not None:
                    mSR.BME680WriteI2c(dataOut,dateTime)
            print("=======================")    
            time.sleep(2.5)   

            startTime = mSR.delayMints(time.time() - startTime,loopInterval)

        except Exception as e:
            print(e)
    		
            break   


if __name__ == "__main__":
   main()