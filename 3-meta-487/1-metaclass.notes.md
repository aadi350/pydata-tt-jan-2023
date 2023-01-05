# Metaclasses
These are notes, use the python file to demonstrate 

Metaclasses are a callable that returns a class
type(classname, bases, namespace) returns a class

Classes "create" instances, metaclasses create classes, python is dynamic

A metaclass is a "class" of a "class", class is an instance of a metaclass
This is a stupic example


Three step process to define a metaclass:
1. Before new/init, prepare called (if defined), used to return dicitonary to contain eveything in namepsace in class, so we could define custom dictionaries (e.g. OrderedDict)
2. new(mcs, name, bases, classdict) analagous to new in classes, but with more arguments, this CREATES the class `type.__new__`, could add/filter out things that we want/don't want in the class
3. init is POST-processing of class


Keyword arguments allow customization, name not special, passed to new/init, up to metaclass to what to do with data (e.g. stripping out all __dunder__ attributes, etc)

Metaclasses create classes, NOT objects
```python
class BaseMeta(type):
	def __new__(cls, classname, bases, namespace):
		print(cls, classname, bases, namespace)		
		return type.__new__(cls, classname, bases, namespace)

	def __prepare__(name, *bases, **kwargs):
		return {}

class A(metaclass=BaseMeta):
	def __init__(self, *args, **kwargs):
		print('A __init__')

a = A()

```

- `Metaclass.__prepare__` returns the namespace 
- `Metaclass.__new__` returns the Class object
- `Metaclass.__call__` returns whatever Metaclass.__new__ returned 

Applications of metaclasses (prior 487):
1. Registering class definition
2. Initialize attributes
3. Modify classes
4. Ensure subclass implementation



