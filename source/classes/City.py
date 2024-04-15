from TrafficObject import TrafficObject
from classes.Controls.SensorObject import SensorObject
g_instance = None


class City(object):
    def __init__(self, name: str = ''):
        global g_instance   # Singletone principle
        g_instance = self   # храним глобальную ссылку на единственный такой объект

        self.name: str = name
        self.c_transport: list[TrafficObject] = []  # Storage of transport
        self.c_sensors: list[SensorObject] = []     # Storage of sensors
