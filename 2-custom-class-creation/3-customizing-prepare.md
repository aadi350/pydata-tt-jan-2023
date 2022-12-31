# Customizing Prepare

```python
class C:
	a : int = 10 
	def __init__(self, *args, **kwargs):
		self.b = kwargs.get('b', None)
	
	def baz(self, ):
		return baz

```

`type(classname, bases, namespace)`

```python
type(
	'C',
	(object, ),
	{
		'__init__': 
	}
)
