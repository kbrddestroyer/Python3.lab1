import json
from pydoc import locate
import classes


class ISerializable(object):
    def __init__(self, **kwargs):
        assert classes.g_saver is not None
        classes.g_saver.register(self)
        data = kwargs.get('data', None)
        if data is None:
            return

        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __del__(self):
        classes.g_saver.unregister(self)

    def getJSON(self):
        return vars(self)


class SystemSaver(object):
    FILENAME = 'test.json'
    DELAYED_TYPES = (
        'classes.City.City',
        'classes.SmartCity',
    )

    def __init__(self):
        self.__serializables: list[ISerializable] = []

    def register(self, serializable):
        self.__serializables.append(serializable)

    def unregister(self, serializable):
        self.__serializables.remove(serializable)

    def save(self):
        output = open(self.FILENAME, 'w')
        blob = {}
        for serializable in self.__serializables:
            key = f'{serializable.__class__.__module__}.{serializable.__class__.__name__}'
            if key not in blob.keys():
                blob[key] = []
            blob[key].append(serializable.getJSON())
        output.write(json.dumps(blob, indent=4))
        output.close()
        print('saved')

    def load(self):
        input = open(self.FILENAME, 'r')
        rawData = input.read()
        if len(rawData) == 0:
            return []

        data = json.loads(rawData)

        result = []     # Result pool
        delayed = []    # Delayer creation pool

        # Весь прикол инициализации из JSON-файла заключается в том
        # что некоторые объекты завязаны на других
        # НАПРИМЕР - City хранит список TrafficObject-ов
        #
        # таким образом выше мы создали пул объектов, которые должны созлаваться исключительно
        # в конце инициализаци, чтобы иметь возможность получить необходимые объекты из уже
        # сформированных локальных пулов

        for classname, settings in data.items():
            driver = locate(classname)
            if classname in self.DELAYED_TYPES:
                delayed.append((driver, settings))
                continue
            assert driver is not None
            for setting in settings:
                result.append(driver(data=setting))

        for driver, settings in delayed:
            for setting in settings:
                result.append(driver(data=setting))
        return result


classes.g_saver = SystemSaver()
