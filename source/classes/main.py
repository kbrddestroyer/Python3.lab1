from classes.City import City
from SystemSaver.SystemSaver import *

if __name__ == "__main__":
    result = g_saver.load()

    for res in result:
        print(res)