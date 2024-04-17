from City import City
from classes.Controls.SensorObject import SensorObject, g_sensorObjectPool
from classes.Controls.Sensors.GasSensor import GasSensor, POLLUTION_LEVEL


class SensorDictWrapper(dict):
    def __init__(self, c_dict):
        super(SensorDictWrapper, self).__init__(c_dict)

    def __getitem__(self, item):
        return g_sensorObjectPool[super().__getitem__(item)]


class SmartCity(City):
    def __init__(self, **kwargs):
        self.c_sensors = {GasSensor: GasSensor().id}     # Storage of sensors
        super(SmartCity, self).__init__(**kwargs)
        self.sensors = SensorDictWrapper(self.c_sensors)

    def onVehicleAdded(self, pollution):
        for sensor in self.sensors:
            if type(sensor) is GasSensor:
                sensor.onAddVehicle(pollution)

    def onVehicleRemoved(self, pollution):
        for sensor in self.sensors:
            if type(sensor) is GasSensor:
                sensor.onRemoveVehicle(pollution)