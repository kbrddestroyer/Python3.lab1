from SystemSaver.SystemSaver import ISerializable


class TrafficObject(ISerializable):
    ID = 0

    def __init__(self, **kwargs):
        super(TrafficObject, self).__init__(**kwargs)
        self.__id = self.ID
        self.ID += 1

    @property
    def id(self):
        return self.__id