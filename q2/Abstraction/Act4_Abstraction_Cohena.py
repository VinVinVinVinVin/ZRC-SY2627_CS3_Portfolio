from abc import ABC, abstractmethod 

class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass

class PHSensor(Sensor):
    def get_reading(self):
        return "[pH Sensor] Reading: 7.2 pH (Neutral)"

class TempSensor(Sensor):
    def get_reading(self):
        return "[Temperature Sensor] Reading: 24.5°C"


if __name__ == "__main__":
    print("--- Lab Inventory System ---")
    
    sensors = [
        PHSensor(),
        TempSensor()
    ]

    for s in sensors:
        print(s.get_reading())

my_sensor = Sensor()