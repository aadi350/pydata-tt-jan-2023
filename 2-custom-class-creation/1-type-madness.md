# Objects

## How Types Work
```python
class Base: pass

b = Base()
print(type(b))
# <class '__main__.Base'>

print(type(Base))
# <class 'type'>

```

## Creating Classes
```python
class A: 
	a = 1
	b = 'hello'
	def f(self, ):
		return self.a

print('hello')

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

When a class definition is executed, the following steps occur:  
- MRO entries are resolved;  
- the appropriate metaclass is determined;  
- the class namespace is prepared;  
- the class body is executed;  
- the class object is created.  

A namespace is a collection of currently defined symbolic names along with information about the object that each name references. You can think of a namespace as a dictionary in which the keys are the object names and the values are the objects themselves

The point of this example is to show that the Python runtime is rich, and we can potentially hook into background processes
