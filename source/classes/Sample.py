if __name__ == "__main__":
    pass                    # Пустая команда, ничего не делвет

    _: int = 0
    _: float = 0.0
    _: bool = True # False
    _: str = 'Hello'
    _: str = "Hello"
    _: list = []
    _: dict = {}
    _: tuple = (1, 2, 3)


    class Class(object):
        STATIC = 0

        def __init__(self):
            print('Hello')
            self.a = 0
            self.b = 0

        def __del__(self):
            print('RIP')

        def __str__(self):
            return f'{self.a}, {self.b}'

        def _func(self):
            pass

    class ChildClass(Class):
        def __init__(self):
            super(ChildClass, self).__init__()

        def func(self):
            super(ChildClass, self)._func()

        @staticmethod
        def static():
            print('Static hello!')

        @property
        def A(self):
            return self.a
