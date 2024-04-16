import TrafficObject


class Car(TrafficObject):
    def __init__(self, speed: float = 0, capacity: int = 1, name: str = "", data: dict = None):
        super(Car, self).__init__()
        self.__speed = speed
        self.__capacity = capacity
        self.__name = name
