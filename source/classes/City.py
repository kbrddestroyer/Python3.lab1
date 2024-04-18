from classes.SystemSaver.SystemSaver import ISerializable
from classes.TrafficObject import TrafficObject
import classes.globals as globals


class TransportListWrapper(object):
    # Класс-обертка для списка с ID TrafficObject-ов
    # используется для получения объекта по ID
    def __init__(self, c_list, root):
        self.root: City = root
        self.c_list = c_list

    def __getitem__(self, item):
        # operator []
        return globals.g_trafficObjectPool[self.c_list[item]]

    def __iter__(self):
        # Для использования в циклах в качестве аргумента
        yield from [x for x in globals.g_trafficObjectPool.values() if x.id in self.c_list]

    def __len__(self):
        return len(self.c_list)

    def removeById(self, __id: int):
        self.c_list.remove(self.c_list[__id])

    def append(self, __object: TrafficObject):
        self.c_list.append(__object.id)
        if hasattr(self.root, 'onVehicleAdded'):
            self.root.onVehicleAdded(__object.pollution)    # Уведомление сервисам

    def remove(self, __value: TrafficObject):
        self.c_list.remove(__value.id)
        if hasattr(self.root, 'onVehicleRemoved'):
            self.root.onVehicleRemoved()                    # Уведомление сервисам


class City(ISerializable):
    def __init__(self, **kwargs):
        self.name: str = kwargs.get('name', 'undefined')
        self.c_transport: list[TrafficObject] = []          # ID всего связанного транспорта
        super(City, self).__init__(**kwargs)

    @property
    def transport(self):
        return TransportListWrapper(self.c_transport, self)

    def __str__(self):
        return f'NAME: {self.name}\n' \
               f'TOTAL TRANSPORT: {len(self.c_transport)}'
