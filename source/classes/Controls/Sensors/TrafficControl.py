from classes.Controls.SensorObject import SensorObject
from classes.TrafficObject import TrafficObject


class TrafficControl(SensorObject):
    def __init__(self, **kwargs):
        self.__passengerFlow = 0
        super(TrafficControl, self).__init__(**kwargs)

    def countPassengerFlow(self, vehicles: list[TrafficObject]):
        for vehicle in vehicles:
            self.__passengerFlow += vehicle.capacity
        self.__passengerFlow /= len(vehicles)
        return self.__passengerFlow

    @property
    def passengerFlow(self):
        return self.__passengerFlow

    @staticmethod
    def addVehicle(listWrapper: list[TrafficObject], trafficObject: TrafficObject):
        listWrapper.append(trafficObject)

    @staticmethod
    def removeVehicle(listWrapper: list[TrafficObject], trafficObject: TrafficObject):
        listWrapper.remove(trafficObject)
