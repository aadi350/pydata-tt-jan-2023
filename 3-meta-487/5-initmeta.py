# InitMeta.py

# this is annoying
class A:
    def __init__(self, a, b, c, d, e, f, g):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g

# Metaclasses to the rescue!
class InitMeta(type):
    import inspect

    def __new__(cls, name, bases, attributes):
        if not (cls_init := attributes.get('__init__', None)):
            raise RuntimeError('__init__ must be specified')

        init_args = list(InitMeta.inspect.signature(cls_init).parameters.keys())[1:]

        def meta_init(self, *args, **kwargs):
            # set kwargs first, else non-kwarg is overritten by get() returning None
            for arg in init_args:
                setattr(self, arg, kwargs.get(arg))

            for arg_name, arg in zip(init_args, args):
                setattr(self, arg_name, arg)


            cls_init(self, *args, **kwargs)

        attributes['__init__'] = meta_init

        return super(InitMeta, cls).__new__(cls, name, bases, attributes)


class A(metaclass=InitMeta):
    def __init__(self, a, b):

        print(self.a)
