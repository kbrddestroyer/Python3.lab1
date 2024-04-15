g_saver = None


class SystemSaver(object):
    def __init__(self):
        global g_saver
        g_saver = self