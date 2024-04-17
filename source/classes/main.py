from classes.City import City
from classes.SmartCity import SmartCity
from classes.Car import Car
from SystemSaver.SystemSaver import *


class Main(object):
    def __init__(self):
        self.g_saver = classes.g_saver
        self.__data = self.g_saver.load()
        pass

    def __del__(self):
        self.g_saver.save()


if __name__ == "__main__":
    Main()
