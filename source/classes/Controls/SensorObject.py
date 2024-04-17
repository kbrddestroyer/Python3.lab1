from classes.SystemSaver.SystemSaver import ISerializable

g_sensorObjectPool = {}


class SensorObject(ISerializable):
    ID = 0

    def __init__(self, **kwargs):
        global g_sensorObjectPool
        self.__id = SensorObject.ID
        SensorObject.ID += 1
        super(SensorObject, self).__init__(**kwargs)

        g_sensorObjectPool[self.__id] = self

    @property
    def id(self):
        return self.__id
