from classes.SmartCity import SmartCity
from TrafficObject import TrafficObject
from TrafficSystem.Car import Car
from TrafficSystem.PublicTransport import PublicTransport
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
                    continue
                if key not in self.__city.sensors.keys():
                    print('Sensor not found')
                print(self.__city.sensors[key])
            elif key == '5':
                self.__addTransport()
            input()

    def __displayMenu(self):
        print('MENU: ')
        print('1. Print city information')
        print('2. Get transport')
        print('3. Get services')
        print('4. Get sensors')
        print('5. Add transport')
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

    def __addTransport(self):
        print('TRANSPORT MENU')
        print('TYPE: ')
        type = input('(1 - Car | 2 - Public) ')

        ob = None

        name = input('Name your transport: ')
        if type == '1':
            manufacturer = input('Manufacturer: ')
            ob = Car(name=name, manufacturer=manufacturer)
        elif type == '2':
            tr_type = input('Type: ')
            route = input('Route No: ')
            ob = PublicTransport(name=name, route=route, type=tr_type)
        else:
            print('Invalid type. Try again')
        self.__city.transport.append(ob)

    def __del__(self):
        self.g_saver.save()


if __name__ == "__main__":
    Main()
