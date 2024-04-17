import enum

from classes.Controls.SensorObject import SensorObject


class POLLUTION_LEVEL(enum.Enum):
    HIGH = 'High'
    AVERAGE = 'Average'
    LOW = 'Low'

    @staticmethod
    def getLevelByMetrics(pollution: float):
        if pollution > 10:
            return POLLUTION_LEVEL.HIGH
        elif pollution > 5:
            return POLLUTION_LEVEL.AVERAGE
        else:
            return POLLUTION_LEVEL.LOW


class GasSensor(SensorObject):
    def __init__(self, **kwargs):
        self.__pollution: float = 0.0
        self.__vehicles: int = 0
        super(GasSensor, self).__init__(**kwargs)

    def onAddVehicle(self, pollution):
        self.__vehicles += 1
        self.__pollution += pollution

    def onRemoveVehicle(self, pollution):
        self.__vehicles -= 1
        self.__pollution -= pollution

    @property
    def averagePollution(self):
        return self.__pollution / self.__vehicles
