from City import City
from classes.Controls.SensorObject import SensorObject, g_sensorObjectPool
from classes.Controls.Sensors.GasSensor import GasSensor, POLLUTION_LEVEL


class SensorListWrapper(list):
    def __init__(self, c_list):
        super(SensorListWrapper, self).__init__(c_list)

    def __getitem__(self, item):
        return g_sensorObjectPool[super().__getitem__(item)]


class SmartCity(City):
    def __init__(self, **kwargs):
        self.c_sensors: list[SensorObject] = [GasSensor().id]     # Storage of sensors
        super(SmartCity, self).__init__(**kwargs)
        self.sensors = SensorListWrapper(self.c_sensors)

    def onVehicleAdded(self, pollution):
        for sensor in self.sensors:
            if type(sensor) is GasSensor:
                sensor.onAddVehicle(pollution)

    def onVehicleRemoved(self, pollution):
        for sensor in self.sensors:
            if type(sensor) is GasSensor:
                sensor.onRemoveVehicle(pollution)