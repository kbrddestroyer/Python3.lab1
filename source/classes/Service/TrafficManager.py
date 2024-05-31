from classes.SmartCity import SmartCity
from classes.Controls.Sensors.TrafficControl import TrafficControl
from classes.TrafficSystem.Car import Car
from classes.TrafficSystem.PublicTransport import PublicTransport

from classes.Service.Service import Service

# Сервисный класс для ввода/вывода информации о транспорте


class TrafficManager(Service):
    def __init__(self, city: SmartCity):
        self.__city = city
        self.__trafficControl: TrafficControl = self.__city.sensors['TrafficControl']
        super(TrafficManager, self).__init__()

    def getTransport(self):
        for ID, transport in enumerate(self.__city.transport):
            print(f'ID: {ID}\n{transport}')

    def addTransport(self):
        print('TRANSPORT MENU')
        print('TYPE: ')
        try:
            type = int(input('(1 - Car | 2 - Public) '))
        except ValueError:
            print('Invalid input data!')
            return

        if type not in (1, 2):
            print('Invalid input data')
            return

        ob = None

        name = input('Name your transport: ')
        capacity = 0
        while capacity <= 0:
            try:
                capacity = int(input('Capacity: '))
            except ValueError:
                capacity = 0
        pollution = 0
        while pollution <= 0:
            try:
                pollution = float(input('Pollution: '))
            except ValueError:
                pollution = 0
        speed = 0
        while speed <= 0:
            try:
                speed = int(input('Speed: '))
            except ValueError:
                speed = 0
        if type == 1:
            manufacturer = input('Manufacturer: ')
            ob = Car(name=name, manufacturer=manufacturer, capacity=capacity, pollution=pollution, speed=speed)
        elif type == 2:
            tr_type = input('Type: ')
            route = input('Route No: ')
            ob = PublicTransport(name=name, route=route, type=tr_type, capacity=capacity, pollution=pollution, speed=speed)

        self.__city.transport.append(ob)

    def removeTransport(self):
        self.getTransport()
        try:
            key = int(input('ID: '))
        except ValueError:
            print('Wrong input!')
            return

        if key >= len(self.__city.c_transport):
            print('Invalid ID')
            return
        transport = self.__city.transport[key]
        self.__city.transport.removeById(key)
        del transport

    def getTrafficControlStats(self):
        self.__trafficControl.countPassengerFlow(self.__city.transport)
        print(self.__trafficControl)

    def __str__(self):
        self.__trafficControl.countPassengerFlow(self.__city.transport)
        return self.__trafficControl.__str__()