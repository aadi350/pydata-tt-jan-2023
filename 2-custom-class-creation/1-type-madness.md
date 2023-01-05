# Objects

## How Types Work
Everything is an object (including classes)
```python
class Base: pass

b = Base()
type(b)

type(Base) # type(some_object) returns class of object

type(type(Base))

```

## Class Definition
What really happens in class creation?
```python 
class SomeClass:
	classvar = 1
	def __init__(self, ):
		self.somevar = 'Some value'

SomeClass.__dict__

```

`type`
```python
class A: 
	a = 1
	b = 'hello'
	def f(self, ):
		return self.a

# OR
def make_A():
    name = 'A'
    bases = ()

    a = 1
    b = 'hello'


    namespace = type.__prepare__(name, bases)

    body = (
'''
a = 1
b = 'hello'

def f(self,):
    return 117
'''
    )
    exec(body, globals(), namespace)

    A = type(name, bases, namespace)
    return A

A = make_A()
a = A()
```

`type` creates a class! By using a custom metaclass (instead of type), we can inject behaviour to classes that would not have been possible

Main takeaway:
`type` is the metaclass that creates classes

## Why does this syntax exist?
```python
import itertools

class A:
	pass

class B:
	pass

class C:
	pass

for parents in itertools.combinations([A, B, C], 2):
	classname = ''.join([c.__name__ for c in parents])
	globals()[classname] = type(classname, parents, {})

	pass
```
