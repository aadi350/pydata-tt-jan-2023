# Technically speaking...
# a callable that creates a class
def dummy_metaclass(classname, bases, namespace):
    return type(classname, bases, namespace)

class MyClass(metaclass=dummy_metaclass):
    pass


# How we actually apply a metaclass
class MyMeta(type):
    pass

class MyClass(MyMeta):
    pass


# Implementing all the methods
class BaseMeta(type):
	def __new__(cls, classname, bases, namespace):
		print(cls, classname, bases, namespace)		
		return type.__new__(cls, classname, bases, namespace)

class A(metaclass=BaseMeta):
	def __init__(self, *args, **kwargs):
		print('A __init__')


# kwargs!
class MyMeta(type):
    def __new__(self, classname, bases, namespace, private):
        if private:
            # do something clever here 
            pass
        return type.__new__(self, classname, bases, namespace)

class MyClass(metaclass=MyMeta, private=True):
    pass


