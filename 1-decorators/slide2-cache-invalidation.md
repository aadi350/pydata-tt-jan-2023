## Applications
### Cache Invalidation

We can cache the result of expensive computations using a decorator

#### Logic
```python
def some_expensive_fn(*args, **kwargs):

	cache = {}
	# if function has seen input before
	if args in cache:
		result = cache[args]
		return result

	# do computations here ONLY if args don't exist in cache 
	result = ...

	return result

```

What's the issue with the above? We don't usually have access to library code!!
	e.g. modifying sklearn's fit() or cv2.dft()

#### Decorators to the Rescue!
```python
def cache(func):
    # Create a cache to store the results of previous function calls
    cache = {}
    
    def wrapper(*args, **kwargs):
        # Check if the function has been called with these arguments before
        if args in cache:
            # If it has, return the cached result
            return cache[args]
        else:
            # If it hasn't, call the function and store the result in the cache
            result = func(*args, **kwargs)
            cache[args] = result
            return result
    
    return wrapper

# we pass our original function into cache()
cached_fn = cache(some_expensive_fn)

# and call exactly as before
cached_fn(*args, **kwargs)
```
