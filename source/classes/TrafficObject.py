from classes.SystemSaver.SystemSaver import ISerializable
import classes.globals as globals

ID = 0

if not hasattr(globals, 'g_trafficObjectPool'):
    globals.g_trafficObjectPool = {}


class TrafficObject(ISerializable):
    def __init__(self, **kwargs):
        global ID
        if not ID:
            ID = 0
        self.__id = ID
        ID += 1

        self.capacity = kwargs.get('capacity', 0)
        self.pollution = kwargs.get('pollution', 0)
        self.speed = kwargs.get('speed', 0)

        super(TrafficObject, self).__init__(**kwargs)

        globals.g_trafficObjectPool[self.__id] = self

    @property
    def id(self):
        return self.__id

    def __str__(self):
        return f'CAPACITY: {self.capacity}\nPOLLUTION PERCENTAGE: {self.pollution * 100}%\nSPEED AVG {self.speed}\n'