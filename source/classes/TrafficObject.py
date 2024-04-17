from SystemSaver.SystemSaver import ISerializable


class TrafficObjectListWrapper(list):
    def __init__(self, r=list(), dft=None):
        pass


class TrafficObject(ISerializable):
    ID = 0

    def __init__(self, **kwargs):
        global g_trafficObjectPool
        super(TrafficObject, self).__init__(**kwargs)

        self.__id = self.ID
        self.ID += 1
        g_trafficObjectPool[id] = self

    @property
    def id(self):
        return self.__id


g_trafficObjectPool = {}
