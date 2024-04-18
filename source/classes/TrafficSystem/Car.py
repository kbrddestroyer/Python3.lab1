from classes.TrafficObject import TrafficObject


class Car(TrafficObject):
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'undefined')
        self.manufacturer = kwargs.get('manufacturer', 'undefined')
        super(Car, self).__init__(**kwargs)

    def __str__(self):
        return f'NAME: {self.name}\nMANUFACTURER: {self.manufacturer}\n{super().__str__()}'
