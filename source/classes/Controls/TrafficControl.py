from ControlObject import ControlObject

g_trafficController = None


class TrafficControl(ControlObject):
    def __init__(self):
        global g_trafficController
        super(TrafficControl, self).__init__()
        g_trafficController = self
