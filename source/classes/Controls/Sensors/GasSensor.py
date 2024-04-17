import enum

from classes.Controls.SensorObject import SensorObject


class POLLUTION_LEVEL(enum.Enum):
    HIGH = 'HIGH'
    AVERAGE = 'AVERAGE'
    LOW = 'LOW'

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
        if self.__vehicles == 0:
            return 0
        return self.__pollution / self.__vehicles

    def __str__(self):
        return f'CITY POLLUTION ESTIMATED AS {POLLUTION_LEVEL.getLevelByMetrics(self.averagePollution).value}'