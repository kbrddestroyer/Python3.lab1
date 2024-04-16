from SystemSaver.SystemSaver import ISerializable
from TrafficObject import TrafficObject, g_trafficObjectPool
from Car import Car


class TransportListWrapper(list):
    def __getitem__(self, item):
        return g_trafficObjectPool[super(TransportListWrapper, self).__getitem__(item)]


class City(ISerializable):
    def __init__(self, name: str = '', **kwargs):
        self.name: str = name
        self.c_transport: list[TrafficObject] = [Car(name="Renault").id]  # Storage of transport
        self.transport = TransportListWrapper()
        super(City, self).__init__(**kwargs)
