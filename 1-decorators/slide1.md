# Returning a Function 

## A Trivial Example
```python
# the function to be returned
def foo(a):
    return a**2

# the function to do the returning 
def baz(f):
	print(f.__name__)
	return f 

foo(4)

foo = baz(foo) 

foo(2)

# syntactic sugar, PEP318
@baz
def foo(a):
	return a**2
```

## Why is this useful

Decorator's ONLY job is to call and return the output of f

General syntax of low-order decorator:
```python
def decorator(f):
    def wrapper(*args, **kwargs):
		# do stuff
        return f(*args, **kwargs) # return f as it was intended
    return wrapper


def foo(a:int):
    return a + 1

foo_decorated = decorator(foo)

print(foo(2))

print(foo_decorated(2))
```


