from classes.Controls.SensorObject import SensorObject


class ElectricitySensor(SensorObject):
    def __init__(self, **kwargs):
        self.electricityFlow: float = kwargs.get('electricityFlow', 1.0)
        super(ElectricitySensor, self).__init__(**kwargs)
        ElectricitySensor.counter = 0

    def tick(self):
        if not ElectricitySensor.counter:
            ElectricitySensor.counter = 0
        ElectricitySensor.counter += 1
        if ElectricitySensor.counter >= 5:
            ElectricitySensor.counter = 0
            self.electricityFlow *= 1.05

    def __str__(self):
        return f'ELECTRICITY FLOW: {self.electricityFlow * 100}%'
