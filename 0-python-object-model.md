This example uses tmux and showing the output interactively in a vertical split
Start with example adding integers and strings


Some class, need to do some mathematical operation
Start with blank class, creating polynomials, with coefficients

Want to be able to do simple operations (show from) :
```python
class Complex: pass

c = Complex()
c.real = 2
c.imag = 3
```
we add init() method

printing looks ugly (add repr), gives printable representaiton of class

We want to add things, add `__add__`

Pattern: we have some behaviour that we want to implement, and we add it using dunder methods, known as "DATA MODEL" methods

Pattern is more about methods, whenever we wish to implement something, we see thepattern:

Top-level function/syntax -> corresponding lower-level dunder function

x + y -> __init__
repr(x) -> __repr__
len(x) -> __len__
x() -> __call__

size of complex (len), using sqrt(a^2 + b^2)

Python data model implement protocols with some abstract meaning, whatever makes sense in that context, in each case we have some protocol, some top-level function (or syntax +, len(), etc) and a corresponding underscore
Everything in Python is an object

Three views of OOP in python:
1. Protocol views
2. Builtin inheritance view 
3. Caveats around OOP
