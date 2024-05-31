from classes.City import City
from classes.Controls.SensorObject import g_sensorObjectPool
from classes.Controls.Sensors.GasSensor import GasSensor
from classes.Controls.Sensors.TrafficControl import TrafficControl
from classes.Controls.Sensors.ElectricitySensor import ElectricitySensor


class SensorDictWrapper(object):
    # см. TransportListWrapper
    # то же самое, но для dict
    def __init__(self, c_dict: dict):
        self.c_dict: dict = c_dict

    def __getitem__(self, item):
        return g_sensorObjectPool[self.c_dict[item]]

    def __iter__(self):
        yield from [g_sensorObjectPool[x] for x in self.c_dict.values()]

    def __len__(self):
        return len(self.c_dict)

    def keys(self):
        return self.c_dict.keys()

    def values(self):
        return self.c_dict.values()


class SmartCity(City):
    def __init__(self, **kwargs):
        self.c_sensors = {}                         # ID всех сенсоров
        super(SmartCity, self).__init__(**kwargs)
        self.__initSensors()                        # инициализация если сенсоры не обнаружены

    @property
    def sensors(self):
        return SensorDictWrapper(self.c_sensors)    # словарб с прослойкой для получения ссылок сенсоров

    def onVehicleAdded(self, pollution):            # Уведомление сенсора о новом транспортном объекте
        self.sensors['GasSensor'].onAddVehicle(pollution)

    def onVehicleRemoved(self, pollution):          # Уведомление об удалении
        self.sensors['GasSensor'].onRemoveVehicle(pollution)

    def __initSensors(self):
        if len(self.c_sensors) == 0:
            self.c_sensors[GasSensor.__name__] = GasSensor().id
            self.c_sensors[TrafficControl.__name__] = TrafficControl().id
            self.c_sensors[ElectricitySensor.__name__] = ElectricitySensor().id

    def __str__(self):
        return f'{super().__str__()}\n' \
               f'TOTAL SENSORS: {len(self.c_sensors)}'
