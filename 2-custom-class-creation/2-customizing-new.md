# Class Creation

```python
class A:
	# actually creates the instance
    def __new__(cls: type,*args, **kwargs):
        print(f'{cls}.__new__')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        # actually creates the object
		# __new__ determines the type of object to return
        return object().__new__(A, **kwargs)

	# initializes instance
    def __init__(self, *args, **kwargs) -> None:
        print(f'{self}.__init__')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')

a = A()

```

--------------------------------------------------------------------------------

## The Factory Pattern
Let's say we wanted to create an Index based on the type of data input. 
(This is essentially replicating pandas default functionality and something that arises very frequently: 
	creating some instance based on input values):

```python
import numpy as np
import pandas as pd


# normal index
normal_index_data = np.linspace(1, 5, 5)
index = pd.Index(normal_index_data)

print(type(index)) # It automatically created the Float64Index
# pandas.core.indexes.numeric.Float64Index


# with datetimes
datetime_index_data = [
		np.datetime64('2022-12-01'), 
		np.datetime64('2023-01-01'),
		np.datetime64('2023-02-01') 
]

index = pd.Index(datetime_index_data)
type(index) # It detected that the datatype was of datetime64 and adjusted accordingly
# pandas.core.indexes.datetimes.DatetimeIndex
```

How do we determine the `type` at runtime?


How not to do it!
```python
from numpy import datetime, datetime64

class DefaultIndex(list): pass
class DatetimeIndex(list): pass


class DynamicIndex:
	def __init__(self, values):
		if type(values[0]) in (datetime, datetime64):
			self = DatetimeIndex 
		else:
			self = DefaultIndex 

		return self

badindex = DynamicIndex([1, 2, 3])
```

Customize __new__ NOT __init__:

```python
class Index:
    def __new__(cls, values):
        if type(values[0]) in (datetime, datetime64):
            cls = DatetimeIndex
        else:
            cls = DefaultIndex
        return object.__new__(cls) # THIS is where the instance is created

class DefaultIndex(Index, Generic[S]):
    def __init__(self, values: List[S]):
        self.values = values

    def first(self):
        return self.values[0]

index, dt_index = DefaultIndex(normal_index_data), DefaultIndex(datetime_index_data)

# It detected the typye of data input
type(index), type(dt_index)

'''(__main__.DefaultIndex, pandas.core.indexes.datetimes.DatetimeIndex)'''
```

## Singleton
```python
class Singleton:
	_instance = None

	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			print('new instance created')
			cls._instance = super().__new__(cls, *args, **kwargs)
		return cls._instance

s1 = Singleton()

s2 = Singleton()
print(s1 is s2)

```
