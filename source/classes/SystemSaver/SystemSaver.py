import json


class ISerializable(object):
    def __init__(self, data: dict = None):
        assert g_saver is not None
        g_saver.register(self)

        if data is None:
            return
        assert type(data) is dict
        assert data[self.__class__.__name__] is not None
        for key, value in data[self.__class__.__name__].items():
            if hasattr(self, key):
                setattr(self, key, value)

    def getJSON(self):
        return vars(self)


class SystemSaver(object):
    FILENAME = 'test.json'

    def __init__(self):
        self.__serializables: list[ISerializable] = []

    def register(self, serializable):
        self.__serializables.append(serializable)

    def save(self):
        output = open(self.FILENAME, 'w')
        blob = {}
        for serializable in self.__serializables:
            blob[str(serializable.__class__.__name__)] = serializable.getJSON()
        output.write(json.dumps(blob))
        output.close()
        print('saved')


g_saver = SystemSaver()
