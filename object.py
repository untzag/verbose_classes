class Object:

    def __call__(cls, *args, **kwargs):
        obj = cls.__new__(cls, *args, **kwargs)
        if isinstance(obj, cls):
            obj.__init__(*args, **kwargs)
        return obj

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

    def __new__(cls, *args, **kwargs):
        return super(Object, cls).__new__(cls)
