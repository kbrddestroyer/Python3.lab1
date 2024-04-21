from classes.Controls.SensorObject import SensorObject
from classes.TrafficObject import TrafficObject


class TrafficControl(SensorObject):
    def __init__(self, **kwargs):
        self.__passengerFlow = 0
        super(TrafficControl, self).__init__(**kwargs)

    def countPassengerFlow(self, vehicles: list[TrafficObject]):
        if len(vehicles) == 0:
            self.__passengerFlow = 0
            return 0

        for vehicle in vehicles:
            self.__passengerFlow += vehicle.capacity
        self.__passengerFlow /= len(vehicles)
        return self.__passengerFlow

    @property
    def passengerFlow(self):
        return self.__passengerFlow

    def __str__(self):
        return f'PASSENGER FLOW: {self.__passengerFlow} per vehicle'
