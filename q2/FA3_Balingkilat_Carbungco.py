from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass

class TempSensor(Sensor):
    def get_reading(self):
        return "[Temperature Sensor] Reading: 24.5 deg C"
    def __str__(self):
        return "[Temperature Sensor] Reading: 24.5 deg C"

class PHSensor(Sensor):
    def get_reading(self):
        return "[ph Sensor] Reading: 7.2 pH (Neutral)"
    def __str__(self):
        return "Reading: 7.2 pH (Neutral)"

sensor = PHSensor()
print("--- Lab Inventory System ---")
print(sensor.get_reading())
sensor2 = TempSensor()
print(sensor2.get_reading())
print("")
print("----------------------------")
