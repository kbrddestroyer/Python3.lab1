from classes.Controls.SensorObject import SensorObject


class ElectricitySensor(SensorObject):
    def __init__(self, **kwargs):
        self.electricityFlow: float = kwargs.get('electricityFlow', 1.0)
        self.counter = 0
        super(ElectricitySensor, self).__init__(**kwargs)

    def tick(self):
        if not self.counter:
            self.counter = 0
        self.counter += 1
        if self.counter >= 5:
            self.counter = 0
            self.electricityFlow *= 1.05

    def __str__(self):
        return f'ELECTRICITY FLOW: {self.electricityFlow * 100}%'
