from classes.City import City
from SystemSaver.SystemSaver import *

if __name__ == "__main__":

    city = City(name='Minsk')

    g_saver.save()

    print(city.getJSON)
