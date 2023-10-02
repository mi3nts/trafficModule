# 1 Download the data 
# Create a data frame for Airmar Data 
import pickle
import datetime
import pandas as pd
#import feather
import glob
import os
from collections import OrderedDict
from functools import reduce
from pandas._libs.tslibs import timestamps
from pandas.core.frame import DataFrame
from yaml.events import CollectionStartEvent
from mintsXU4 import mintsProcessing as mP
from mintsXU4 import mintsDefinitions as mD
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
#import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from mintsXU4 import mintsProcessing as mP

nodeID               = mD.nodeID
airMarID             = mD.airMarID
climateTargets       = mD.climateTargets
rawPklsFolder        = mD.rawPklsFolder
referencePklsFolder  = mD.referencePklsFolder
mergedPklsFolder     = mD.mergedPklsFolder
modelsPklsFolder     = mD.modelsPklsFolder
climateSensors       = mD.climateSensors

dateNow = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
print("Current Time:",dateNow)

for climateSensor in climateSensors:
    print(" ")
    print("=====================MINTS=====================")
    print("Climate data Calibration for Node: " + nodeID +" with Climate Sensor: " + climateSensor)
    print("-----------------------------------------------")
    mintsData = pd.read_pickle(mP.getPathGeneric(mergedPklsFolder,nodeID,climateSensor,"pkl"))
    mP.climateCalibrationV2(nodeID,dateNow, mintsData,climateTargets,climateSensor)
    
    # try:
   
    # except Exception as e:
    #     print("[ERROR] Could not publish data, error: {}".format(e))
    
