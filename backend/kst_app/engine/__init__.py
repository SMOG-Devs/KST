class Engine:
    _initialized = False
    _engine = None

    #     create class constructor
    def __init__(self):
        if not Engine._initialized:
            Engine._engine = 'neural network'
            Engine._initialized = True

    # co  to jest?
    def __str__(self):
        return self._engine

    def flas(self):
        return self._engine
