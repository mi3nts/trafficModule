

from datetime import timedelta
import logging
import smbus2
import struct
import time
import bme280


# to_s16 = lambda x: (x + 2**15) % 2**16 - 2**15
# to_u16 = lambda x: x % 2**16

BME280_I2C_ADDR = 0x76

class BME280:

    def __init__(self, i2c_dev,debugIn):
        
        self.i2c_addr = BME280_I2C_ADDR
        self.i2c      = i2c_dev
        self.debug    = debugIn

    def initiate(self,retriesIn):
        ready = None
        while ready is None and retriesIn:
            try:
                self.calibration_params = bme280.load_calibration_params(self.i2c, self.i2c_addr)
                ready = True
                
            except OSError:
                pass
            time.sleep(1)
            retriesIn -= 1

        if not retriesIn:
            time.sleep(1)
            return False
        
        else:
            print("BME 280 Found - Calibraion Params Set")
            time.sleep(1)
            return True       
      
    def read(self):
        measurement = bme280.sample(self.i2c, self.i2c_addr, self.calibration_params)
        if measurement is not None:
            A = measurement.pressure*100 / 101325;
            B = 1 / 5.25588;
            C = pow(A, B);
            C = 1.0 - C;
            altitude = C / 0.0000225577;
            print("Temperature: {:.2f}'C, Pressure: {:.2f}'P, Relative Humidity: {:.2f}%,  Altitude: {:.2f}m".format(measurement.temperature,measurement.pressure,measurement.humidity,altitude))
            time.sleep(1)
            return [measurement.temperature,measurement.pressure*100,measurement.humidity,altitude];
        else:
            time.sleep(1)
            print("BME280 Measurments not read")    
            return;
