from SystemSaver.SystemSaver import ISerializable
from TrafficObject import TrafficObject
from Car import Car
from classes.Controls.SensorObject import SensorObject


class City(ISerializable):
    def __init__(self, name: str = '', **kwargs):
        self.name: str = name
        self.c_transport: list[TrafficObject] = []  # Storage of transport
        self.c_sensors: list[SensorObject] = []     # Storage of sensors

        super(City, self).__init__(**kwargs)

    def getJSON(self):
        result = vars(self)

        result['c_transport'] = [x.id for x in self.c_transport]
        result['c_sensors'] = [vars(x) for x in self.c_sensors]
        return result
