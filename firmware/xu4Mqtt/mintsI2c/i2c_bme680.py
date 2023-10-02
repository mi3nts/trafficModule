
from datetime import timedelta
import logging
import smbus2
import struct
import time
import bme680

class BME680:

    def __init__(self, i2c_dev,debugIn):
        self.i2c_addr = bme680.I2C_ADDR_SECONDARY
        self.i2c      = i2c_dev
        self.debug    = debugIn

    def initiate(self,retriesIn):
        ready = None
        while ready is None and retriesIn:
            try:
                BME680.sensor = bme680.BME680(self.i2c_addr,self.i2c)

                if self.debug:
                    print('Calibration data:')
                    for name in dir(BME680.sensor.calibration_data):
                        if not name.startswith('_'):
                            value = getattr(BME680.sensor.calibration_data, name)

                            if isinstance(value, int):
                                print('{}: {}'.format(name, value))

                BME680.sensor.set_humidity_oversample(bme680.OS_2X)
                BME680.sensor.set_pressure_oversample(bme680.OS_4X)
                BME680.sensor.set_temperature_oversample(bme680.OS_8X)
                BME680.sensor.set_filter(bme680.FILTER_SIZE_3)
                BME680.sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)

                print('\n\nInitial reading:')
                for name in dir(BME680.sensor.data):
                    value = getattr(BME680.sensor.data, name)
                    if self.debug:
                        if not name.startswith('_'):
                            print('{}: {}'.format(name, value))

                BME680.sensor.set_gas_heater_temperature(320)
                BME680.sensor.set_gas_heater_duration(150)
                BME680.sensor.select_gas_heater_profile(0)
                ready = True
                
            except OSError:
                pass
            time.sleep(1)
            retriesIn -= 1

        if not retriesIn:
            time.sleep(1)
            return False
        
        else:
            print("BME 680 Found - Calibraion Params Set")
            time.sleep(1)
            return True       
      
    def read(self):
        if BME680.sensor.get_sensor_data():
            temperature = BME680.sensor.data.temperature,
            pressure    = BME680.sensor.data.pressure/10,
            humidity    = BME680.sensor.data.humidity
            if BME680.sensor.data.heat_stable:
                gas = BME680.sensor.data.gas_resistance/100
            else:
                gas = -1
            
            print("Temperature: {:.2f}'C, Pressure: {:.2f}'P, Relative Humidity: {:.2f}%, Gas: {:.2f}".format\
                  (temperature[0],pressure[0],humidity,gas))

        
            return [temperature[0],pressure[0],humidity, gas];

        else:
            time.sleep(1)
            print("BME680 Measurments not read")    
            return;

