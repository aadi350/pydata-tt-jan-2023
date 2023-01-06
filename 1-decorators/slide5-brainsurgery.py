class BaseClass:
    pass

class LibraryClassOne(BaseClass):
    pass

class LibraryClassTwo(BaseClass):
    pass

class LibraryClassThree(BaseClass):
    pass

# some requirement comes up
# we need to log every function call to logstash

# Option 1: Editing EVERY library function

# Option 2: Decorating Every Library Function

# Option 3: Decorating the Classes

def _log(msg):
    # log to logstash
    print('From logger: ', msg)

def debugattr(cls):
    orig_gettattribute = cls.__getattribute__

    def __getattribute__(self, name):
        _log(name)
        return orig_gettattribute(self, name)

    cls.__getattribute__ = __getattribute__
    
    return cls

@debugattr
class A:
    def __init__(self,):
        pass

    def foo(self, ):
        pass

# why does this work?
getattr(a, 'foo') # <-high-level
A.__getattribute__('foo') # low-level data model

# does not apply to all classes!
