from classes.City import City
from SystemSaver.SystemSaver import *

if __name__ == "__main__":
    file = open('test.json', 'r')
    city = City(data=json.loads(file.read()))

