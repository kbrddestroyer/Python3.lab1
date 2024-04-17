from classes.SmartCity import SmartCity
from SystemSaver.SystemSaver import *


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
                    return
                if key not in self.__city.sensors.keys():
                    print('Sensor not found')
                print(self.__city.sensors[key])
            input()

    def __displayMenu(self):
        print('MENU: ')
        print('1. Print city information')
        print('2. Get transport')
        print('3. Get services')
        print('4. Get sensors')
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
        for transport in self.__city.transport:
            print(transport)

    def __del__(self):
        self.g_saver.save()


if __name__ == "__main__":
    Main()
