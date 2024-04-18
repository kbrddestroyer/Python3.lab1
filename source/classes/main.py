from classes.SmartCity import SmartCity
from TrafficObject import TrafficObject
from TrafficSystem.Car import Car
from TrafficSystem.PublicTransport import PublicTransport
from SystemSaver.SystemSaver import *

from Controls.TrafficManager import TrafficManager

class Main(object):
    EXIT = 'q'

    def __init__(self):
        self.g_saver = classes.g_saver
        self.__data = self.g_saver.load()

        self.__city = None
        for data in self.__data:
            if isinstance(data, SmartCity):
                self.__city = data

        if self.__city is None:
            self.__initCity()
        self.__trafficManager = TrafficManager(self.__city)
        self.__loop()

    def __loop(self):
        while True:
            key = self.__displayMenu()

            if key == Main.EXIT:
                return
            elif key == '1':
                print(self.__city)
            elif key == '2':
                self.__getTransport()
            elif key == '3':
                pass
            elif key == '4':
                for k in self.__city.c_sensors.keys():
                    print(k)
                print('REQUEST NAME: (quit to abort)')
                key = input(': ')
                if key.lower() == 'quit':
                    continue
                if key not in self.__city.sensors.keys():
                    print('Sensor not found')
                print(self.__city.sensors[key])
            elif key == '5':
                self.__addTransport()
            elif key == '6':
                self.__trafficManager.removeTransport()
            elif key == '7':
                self.__trafficManager.getTrafficControlStats()

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
        for ID, transport in enumerate(self.__city.transport):
            print(f'ID: {ID}\n{transport}')

    def __addTransport(self):
        self.__trafficManager.addTransport()

    def __del__(self):
        self.g_saver.save()


if __name__ == "__main__":
    Main()
