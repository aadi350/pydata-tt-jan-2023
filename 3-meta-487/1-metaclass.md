# Metaclasses

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
