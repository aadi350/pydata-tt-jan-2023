# PEP 487

Replaces everything a metaclass can do (except for protocol enforcement)

```python
class Parent:
    def __init__(self, *args, **kwargs) -> None:
        print('Parent __init__')

    def __new__(cls, *args, **kwargs):
        print('Parent __new__')
        return super().__new__(cls, *args, **kwargs)

    def __init_subclass__(cls):
        print('__init_subclass__')

class Child(Parent):
    def __init__(self, *args, **kwargs):
        print('Child __init__')
        super().__init__(*args, **kwargs)

child_instance = Child()
```

## Enforcing Type Hints
```python
import inspect

class EnforceTypeHints:
    def __init_subclass__(cls) -> None:
        method_list = inspect.getmembers(cls, predicate=inspect.isfunction)
        for func_name, func in method_list: 
            for arg_name, parameter in list(inspect.signature(func).parameters.items())[1:]:
                t = parameter.annotation
                if t == inspect._empty: raise ValueError(f'Argument {arg_name} needs a type annotation')

class TypeHinted(EnforceTypeHints):
    def __init__(self, a:int) -> None:
        super().__init__()

class BadClass(EnforceTypeHints):
	def __init__(self, a: int):
		pass

```


## Ensuring Method Implementation
```python
class Transformer:
    subclasses = {}
    required_methods = ['transform', 'fit']


    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        cls.subclasses[cls.__name__] = cls

        for method in Transformer.required_methods:
            if not hasattr(cls, method):
                raise NotImplementedError(f'Subclass of Transformer must implement the {method} method')

class GoodTransformer(Transformer):
    def transform(self, ):
        pass

    def fit(self, ):
        pass
    
class BadTransformer(Transformer):
    pass
```
