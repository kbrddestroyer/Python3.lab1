from SystemSaver.SystemSaver import ISerializable
from TrafficObject import TrafficObject, g_trafficObjectPool


class TransportListWrapper(list):
    def __init__(self, c_list, root):
        super(TransportListWrapper, self).__init__(c_list)
        self.root = root

    def __getitem__(self, item):
        return g_trafficObjectPool[super().__getitem__(item)]

    def append(self, __object: TrafficObject):
        super().append(__object.id)
        if hasattr(self.root, 'onVehicleAdded'):
            self.root.onVehicleAdded(__object.pollution)

    def remove(self, __value):
        super().remove(__value)
        if hasattr(self.root, 'onVehicleRemoved'):
            self.root.onVehicleRemoved()


class City(ISerializable):
    def __init__(self, **kwargs):
        self.name: str = kwargs.get('name', 'undefined')
        self.c_transport: list[TrafficObject] = []  # Storage of transport
        super(City, self).__init__(**kwargs)

    @property
    def transport(self):
        return TransportListWrapper(self.c_transport, self)

    def __str__(self):
        return f'NAME: {self.name}\n' \
               f'TOTAL TRANSPORT: {len(self.c_transport)}'