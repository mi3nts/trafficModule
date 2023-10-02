
from getmac import get_mac_address
import serial.tools.list_ports
import pandas as pd

# Added March 1sr 2023: for ports with same names and PID 


def getPathGeneric(dataFolder,nodeID,sensorID,ext):
    writePath = dataFolder+"/"+nodeID+"/"+"MINTS_"+ nodeID+ "_"+sensorID+"." + ext
    # directoryCheck(writePath)
    return writePath;

def findPortV2(inStr,lenStr):
    ports    = list(serial.tools.list_ports.comports())
    outPorts =  []
    for p in ports:
        currentPort = str(p[1])
        if(currentPort.find(inStr)>=0 and len(currentPort)==lenStr):
            outPorts.append(str(p[0]).split(" ")[0])
    return(outPorts)

def findPort(find):
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        currentPort = str(p)
        if(currentPort.endswith(find)):
            return(currentPort.split(" ")[0])

def findIPSPorts():
    ports = list(serial.tools.list_ports.comports())
    ipsPorts = []
    for p in ports:
        currentPort = str(p[2])
        if(currentPort.find("PID=10C4")>=0):
            ipsPorts.append(str(p[0]).split(" ")[0])
    return ipsPorts
  
def findAirmarPort():
    ports = list(serial.tools.list_ports.comports())
    ozonePort = []
    for p in ports:
        currentPort = str(p[2])
        if(currentPort.find("PID=067B")>=0):
            ozonePort.append(str(p[0]).split(" ")[0])
    return ozonePort
  

def findMacAddress():
    macAddress= get_mac_address(interface="eth0")
    if (macAddress!= None):
        return macAddress.replace(":","")

    macAddress= get_mac_address(interface="docker0")
    if (macAddress!= None):
        return macAddress.replace(":","")

    macAddress= get_mac_address(interface="enp1s0")
    if (macAddress!= None):
        return macAddress.replace(":","")

    macAddress= get_mac_address(interface="wlan0")
    if (macAddress!= None):
        return macAddress.replace(":","")

    return "xxxxxxxx"



dataFolderReference       = "/home/teamlary/mintsData/reference"
dataFolderMQTTReference   = "/home/teamlary/mintsData/referenceMQTT"
dataFolder                = "/home/teamlary/mintsData/raw"
dataFolderMQTT            = "/home/teamlary/mintsData/rawMQTT"

dataFolderPre             = "/home/teamlary/mintsData"
rawPklsFolder             = dataFolderPre + "/rawPkls"
referencePklsFolder       = dataFolderPre + "/referencePkls"
mergedPklsFolder          = dataFolderPre + "/mergedPkls"
modelsPklsFolder          = dataFolderPre + "/modelsPkls"
dataFolderCC              = dataFolderPre + "/climateCalibrated"

liveFolder                = dataFolderPre + "/liveUpdate/results"

# Change Accordingly  

dataFolderMQTTCalib       = dataFolderPre + "/calibratedMQTT"
timeSpan                  = 30



macAddress            = findMacAddress()
nodeID                = macAddress
airMarID              = "001e0610c0e4"

latestDisplayOn       = False
latestOn              = False

airmarPorts           = findPortV2("USB-Serial Controller D",23)
rg15Ports             = findPortV2("USB-Serial Controller",21)
canareePorts          = findPortV2("Canaree PM",10)

ipsPorts              = ["/dev/ttyS1"]
climateSensors        = ["BME280","BME680","SCD30"]
climateTargets        = ["WIMDA_airTemperature","WIMDA_barrometricPressureBars","WIMDA_relativeHumidity","WIMDA_dewPoint","YXXDR_barrometricPressureBars"]

# For MQTT 
mqttOn                = True
mqttCredentialsFile   = 'mintsXU4/credentials.yml'
mqttBroker            = "mqtt.circ.utdallas.edu"
mqttPort              =  8883  # Secure port



mdls = {}

for target in climateTargets:
    for climateSensor in climateSensors:
        mdls[target +"_" +climateSensor + "_MDL"] = pd.read_pickle(getPathGeneric(modelsPklsFolder,nodeID,target+"_MDL_"+climateSensor,"pkl"));

if __name__ == "__main__":
    # the following code is for debugging
    # to make sure everything is working run python3 mintsDefinitions.py 
    print("Mac Address                : {0}".format(macAddress))
    print("Data Folder Reference      : {0}".format(dataFolderReference))
    print("Data Folder Raw            : {0}".format(dataFolder))
    print("Latest On                  : {0}".format(latestOn))
    print("MQTT On                    : {0}".format(mqttOn))
    print("MQTT Credentials File      : {0}".format(mqttCredentialsFile))
    print("MQTT Broker and Port       : {0}, {1}".format(mqttOn,mqttPort))

    print("IPS Ports:")
    for dev in ipsPorts:
        print("\t{0}".format(dev))


