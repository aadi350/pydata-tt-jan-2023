# Decorators

In order to set some context, we need to look at python functions 
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
Python has first-class functions:
- You can assign functions to variables
- Pass functions as arguments to other functions (like you do with variables)
- A function can be returned by other function

