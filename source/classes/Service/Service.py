import classes.globals as globals

if not globals.g_services:
    globals.g_services = {}


class Service(object):
    def __init__(self):
        globals.g_services[self.__class__.__name__] = self
