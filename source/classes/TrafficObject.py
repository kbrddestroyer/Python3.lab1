from SystemSaver.SystemSaver import ISerializable

g_trafficObjectPool = {}


class TrafficObject(ISerializable):
    ID = 0

    def __init__(self, **kwargs):
        global g_trafficObjectPool
        self.__id = self.ID
        self.ID += 1

        self.capacity = kwargs.get('capacity', 0)
        self.pollution = kwargs.get('pollution', 0)
        self.speed = kwargs.get('speed', 0)

        super(TrafficObject, self).__init__(**kwargs)

        g_trafficObjectPool[self.__id] = self

    @property
    def id(self):
        return self.__id

    def __str__(self):
        return f'CAPACITY: {self.capacity}\nPOLLUTION PERCENTAGE: {self.pollution * 100}%\nSPEED AVG {self.speed}\n'