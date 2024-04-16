from classes.City import City
from SystemSaver.SystemSaver import *

if __name__ == "__main__":
    res = g_saver.load()
    print(res[1].transport[0])