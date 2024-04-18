from classes.City import City
from classes.Controls.SensorObject import g_sensorObjectPool
from classes.Controls.Sensors.GasSensor import GasSensor
from classes.Controls.Sensors.TrafficControl import TrafficControl


class SensorDictWrapper(dict):
    def __init__(self, c_dict):
        super(SensorDictWrapper, self).__init__(c_dict)

    def __getitem__(self, item):
        return g_sensorObjectPool[super().__getitem__(item)]


class SmartCity(City):
    def __init__(self, **kwargs):
        self.c_sensors = {}     # Storage of sensors
        super(SmartCity, self).__init__(**kwargs)
        self.__initSensors()

    @property
    def sensors(self):
        return SensorDictWrapper(self.c_sensors)

    def onVehicleAdded(self, pollution):
        for sensor in self.sensors:
            if type(sensor) is GasSensor:
                sensor.onAddVehicle(pollution)

    def onVehicleRemoved(self, pollution):
        for sensor in self.sensors:
            if type(sensor) is GasSensor:
                sensor.onRemoveVehicle(pollution)

    def __initSensors(self):
        if len(self.c_sensors) == 0:
            self.c_sensors[GasSensor.__name__] = GasSensor().id
            self.c_sensors[TrafficControl.__name__] = TrafficControl().id

    def __str__(self):
        return f'{super().__str__()}\n' \
               f'TOTAL SENSORS: {len(self.c_sensors)}'
