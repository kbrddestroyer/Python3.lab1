from City import City
from classes.Controls.SensorObject import SensorObject, g_sensorObjectPool
from classes.Controls.Sensors.GasSensor import GasSensor, POLLUTION_LEVEL

class SmartCity(City):
    def __init__(self, **kwargs):
        self.c_sensors: list[SensorObject] = [GasSensor().id,]     # Storage of sensors

        super(SmartCity, self).__init__(**kwargs)
