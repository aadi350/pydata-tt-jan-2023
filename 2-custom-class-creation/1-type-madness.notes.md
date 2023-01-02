## How Types Work
If you've been programming in Python for a while, you might know that everything is an object, and classes create objects. But if everything is an object (and classes are also objects), who creates those classes? This is exactly the question that I answer.

Everything is an object in Python, and they are all either instances of classes or instances of metaclasses, except for type.

type is itself a class, and it is its own type. It's a metaclass. A metaclass instantiates and defines behavior for a class just like a class instantiates and defines behavior for an instance.

## Class Definition
A class in Python is executable code, dynamically run with nearly no static information (e.g. a loop inside a class) as opposed to just a frame of methods in C++/Java classes

Here's what happens whenever the keyword class is encountered:

instance methods are created when called, callbacks with strong-references hold the objects in memory

The body (statements and functions) of the class is isolated.
The namespace dictionary of the class is created (but not populated yet).
The body of the class executes, then the namespace dictionary is populated with all of the attributes, methods defined, and some additional useful info about the class.
The metaclass is identified in the base classes or the metaclass hooks (explained later) of the class to be created.
The metaclass is then called with the name, bases, and attributes of the class to instantiate it.
And because type is the default metaclass in Python, you can use type to create classes in Python.

type, when called with one argument, produces the type information of an existing class. type called with three arguments creates a new class object. The arguments, when invoking type, are the name of the class, a list of base classes, and a dictionary giving the namespace for the class (all the fields and methods).

Why does this syntax exist? let's say we have three classes (A, B, C), and (for some reason), we need compositions of all three (AB, BC, AC), Python is dynamic, so we could theoretically do this (example using itertools), show bases, etc
	"Matrices" of classes
