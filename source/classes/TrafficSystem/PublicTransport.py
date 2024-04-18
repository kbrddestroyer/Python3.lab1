from classes.TrafficObject import TrafficObject

# Наследник TrafficObject
# Выступает в роли модели общественного транспорта в городе

class PublicTransport(TrafficObject):
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'undefined')
        self.type = kwargs.get('type', 'undefined')
        self.route = kwargs.get('route', 'undefined')
        super(PublicTransport, self).__init__(**kwargs)
