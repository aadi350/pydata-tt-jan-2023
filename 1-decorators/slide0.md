# Decorators

In order to set some context, we need to look at python functions 
Explain def , function name, args, kwargs, and output

```python
# anatomy of a function
def foo(*args, **kwargs):
    # do something useful
    return output

# return a string
def return_a_string():
    return 'a'
print(return_a_string())

def return_an_int():
    return -1 
print(return_an_int())

def return_object():
	class A: pass
	a = A()
	return a
print(return_object())
```


