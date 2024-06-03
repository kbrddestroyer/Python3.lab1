import json
from pydoc import locate
import classes

# ТУТ НАЧИНАЕТСЯ МАГИЯ АВТОМАТИЧЕСКОГО СОХРАНЕНИЯ
# Система работает следующим образом: когда ты создаешь класс,
# который планируется сохранять в файл, нужно отнаследовать его от ISerializable
# Таким образом он начнет включать всю логику этого класса
# ISerializable построен таким образом, что при вызове его конструктора
# он помещает экземпляр созданного класса в словарь под тегом класса-наследника
# Если в kwargs конструктора передана data то класс действует иначе
# Помимо размещения в dict скрипт копирует данные из data, которые считается что взяты из
# JSON файла и подготовлены при помощи SystemSaver
#
# SystemSaver - класс отвечающий за работу ввода/вывода в файловую систему
# Для того, чтобы не завязываться на логику каких-либо сторонних пакетов для сериализации
# я сделал простой парсер в JSON
# Благо, Python3 позволяет быстро конвертировать объекты в dict и наоборот
# Для получения словаря из объекта используется функция vars(__ob), которая, по сути, возвращает
# __ob.__dict__()
# Для десериалилзации происходит проход по keys() data и для каждого ключа происходит проверка
# hasattr
# если атрибут есть в классе - он назначается через setattr


class ISerializable(object):
    def __init__(self, **kwargs):
        assert classes.g_saver is not None
        classes.g_saver.register(self)      # Объект помечен к сохранению и добавлен в пул
        data = kwargs.get('data', None)
        if data is None:
            return

        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)   # Собственно, десериализация (см. выше)

    def __del__(self):
        classes.g_saver.unregister(self)    # Удаление из пула если объект удален раньше времени (не будет сохранен)

    def getJSON(self):
        return vars(self)   # Собственно, JSON (см. выше)


class SystemSaver(object):
    FILENAME = 'test.json'      # Файл, куда сохранять и откуда читать
    DELAYED_TYPES = (
        'classes.City.City',
        'classes.SmartCity',    # см. ниже
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
            # Ключ - название класса и модуля
            # например
            # classes.City.City
            key = f'{serializable.__class__.__module__}.{serializable.__class__.__name__}'
            if key not in blob.keys():
                blob[key] = []
            blob[key].append(serializable.getJSON())
        output.write(json.dumps(blob, indent=4))
        output.close()
        print('Saved data file')

    def load(self):
        print(self.FILENAME)
        try:
            inputData = open(self.FILENAME, 'r')
        except FileNotFoundError:
            print('System dump not found. DEFAULT:')
            return []
        rawData = inputData.read()
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
            if classname in SystemSaver.DELAYED_TYPES:
                delayed.append((driver, settings))
                continue
            assert driver is not None
            for setting in settings:
                result.append(driver(data=setting))

        for driver, settings in delayed:
            for setting in settings:
                result.append(driver(data=setting))
        return result

    def __del__(self):
        for serializable in self.__serializables:
            del serializable


classes.g_saver = SystemSaver()
