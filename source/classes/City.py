from SystemSaver.SystemSaver import ISerializable
from TrafficObject import TrafficObject
from classes.Controls.SensorObject import SensorObject

class City(ISerializable):
    def __init__(self, name: str = '', data: dict = None):
        self.name: str = name
        self.c_transport: list[TrafficObject] = []  # Storage of transport
        self.c_sensors: list[SensorObject] = []     # Storage of sensors

        super(City, self).__init__()
