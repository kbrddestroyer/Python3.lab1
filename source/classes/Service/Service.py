import classes.globals

if not hasattr(classes.globals, 'g_services'):
    classes.globals.g_services = {}


class Service(object):
    def __init__(self):
        classes.globals.g_services[self.__class__.__name__] = self

    @staticmethod
    def printServices():
        for name in classes.globals.g_services.keys():
            print(f'{name}')

        name = input('Name: (quit to abort)')
        if name.lower() == 'quit':
            return
        if name not in classes.globals.g_services.keys():
            print('Service not found')

        print(classes.globals.g_services[name])
