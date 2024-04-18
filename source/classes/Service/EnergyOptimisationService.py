from classes.Controls.Sensors.ElectricitySensor import ElectricitySensor
from classes.Service.Service import Service


class EnergyOptimisationService(Service):
    def __init__(self, sensor: ElectricitySensor):
        self.__sensor = sensor
        super(EnergyOptimisationService, self).__init__()

    def optimise(self):
        self.__sensor.electricityFlow *= 0.95

    def __str__(self):
        return self.__sensor.__str__()
