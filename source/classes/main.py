from classes.SmartCity import SmartCity
from classes.Service.EnergyOptimisationService import EnergyOptimisationService
from classes.SystemSaver.SystemSaver import *
from classes.Service.Service import Service

from classes.Service.TrafficManager import TrafficManager

# Это базовый класс всей программы, он определяет основной цикл


class Main(object):
    EXIT = 'q'  # static 

    def __init__(self):
        self.g_saver = classes.g_saver      # Система автосохранения: SystemSaver
        self.__data = self.g_saver.load()   # Данные, получаемые из JSON файла. Словарь объектов. см. SystemSaver

        self.__city = None                  
        for data in self.__data:            # Поиск экземпляра SmartCity
            if isinstance(data, SmartCity):
                self.__city = data

        if self.__city is None:             # Если не найдено
            self.__initCity()

        # Инициализация сервисов (не сохраняются, так как используются для управления и не
        # хранят данные напрямую)
        # Подробнее см. файлы с объявлением
        self.__trafficManager = TrafficManager(self.__city)
        self.__energyOptimisation = EnergyOptimisationService(self.__city.sensors['ElectricitySensor'])
        self.__loop()   # Основной цикл

    def __loop(self):
        while True:
            # -- BANNER DISPLAY --
            key = self.__displayMenu()

            if key == Main.EXIT:
                return
            # PRINT CITY INFORMATION
            elif key == '1':
                print(self.__city)
            # PRINT TRANSPORT
            elif key == '2':
                self.__getTransport()
            # PRINT SERVICES
            elif key == '3':
                Service.printServices()
            # GET SENSORS
            elif key == '4':
                self.__getSensors()
            # ADD TRANSPORT
            elif key == '5':
                self.__addTransport()
            # REMOVE TRANSPORT
            elif key == '6':
                self.__trafficManager.removeTransport()
            # GET STATS -> TRAFFIC
            elif key == '7':
                self.__trafficManager.getTrafficControlStats()
            # OPTIMISE ELECTRICITY FLOW
            elif key == '8':
                self.__optimise()
            # WHOLE INFO TICKET
            elif key == '9':
                self.__ticket()

            # Это добавляет динамики
            # Спустя 5 тиков ElectricitySensor увеличивает потребление энергии
            self.__city.sensors['ElectricitySensor'].tick()

            input('Press any key...')

    def __displayMenu(self):
        print('MENU: ')
        print('1. Print city information')
        print('2. Get transport')
        print('3. Get services')
        print('4. Get sensors')
        print('5. Add transport')
        print('6. Remove transport')
        print('7. Fast traffic stats')
        print('8. Energy flow optimisation')
        print('9. Print data')
        print('q. Quit')
        return input(':')

    def __initCity(self):
        print('Program did not found any CITY entity stored')
        print('Do you want to create one?')
        res = input('(y/n)')
        if res.lower() == 'y':
            name = input('Name your city: ')
            self.__city = SmartCity(name=name)
            print(f'City {name} successfully created')
            print('Welcome, Mayor')
        else:
            print('Aborted by user')
            exit(0)

    def __getTransport(self):
        # enumerate(list[T]) -> dist[int, T]
        for ID, transport in enumerate(self.__city.transport):
            print(f'ID: {ID}\n{transport}')

    def __addTransport(self):
        self.__trafficManager.addTransport()

    def __getSensors(self):
        for k in self.__city.c_sensors.keys():
            print(k)

        # При вводе имени можно получить данные сенсора
        print('REQUEST NAME: (quit to abort)')
        key = input(': ')
        if key.lower() == 'quit':
            return
        if key not in self.__city.sensors.keys():
            print('Sensor not found')
        print(self.__city.sensors[key]) # неявный вызов __str__(self)

    def __optimise(self):
        self.__energyOptimisation.optimise()
        print(f'Optimised electricity flow in {self.__city.name}')
        print(self.__city.sensors['ElectricitySensor'])

    def __ticket(self):
        print('[CITY INFORMATION]')
        print(self.__city)
        print('[SENSORS]')
        print(f'TOTAL: {len(self.__city.sensors)}')
        for sensor in self.__city.sensors:
            print(f'[{str(sensor.__class__.__name__).upper()}]')
            print(sensor)
        print('[TRAFFIC]')
        self.__trafficManager.getTransport()

    def __del__(self):
        self.g_saver.save() # Сохранить данные по завершению


# Это необходимо для вызова Main только при запуске
# и не выполнять этот код при импорте
if __name__ == "__main__":
    Main()      # entrypoint

