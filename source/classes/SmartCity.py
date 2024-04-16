from City import City
from classes.Controls.SensorObject import SensorObject, g_sensorObjectPool


class SmartCity(City):
    def __init__(self, **kwargs):
        self.c_sensors: list[SensorObject] = []     # Storage of sensors
        super(SmartCity, self).__init__(**kwargs)

    def getSensor(self, id):
        assert self.c_sensors[id] in g_sensorObjectPool.keys()
        return g_sensorObjectPool[self.c_transport[id]]
