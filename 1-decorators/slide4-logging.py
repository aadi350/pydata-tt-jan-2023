class BaseLogger:
    def send_usage_data(self, *args, **kwargs):
        pass

class LibraryClass(BaseLogger):
    def baz():
        self.send_usage_data(
                *args, **kwargs)
        

# instead of manually adding logging statements, try-except blocks
# use a decorator

def send_data():
    # complex async LogStash call
    pass

def send_error_data():
    # send error 
    pass

def send_usage_data(func):
    def inner(*args, **kwargs):
        send_data()
        try:
            return func(*args, **kwargs)
        except Exception as e:
            send_error_data()
            raise 

# now I need to add a decorator to EVERY function?!
# NOPE, need a metaclass
import types

def my_logger(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        data['v_errormsg'] = e
        _logger.error("")
        raise

def log_wrapper(func):
    return wraps(func, my_logger)


class LoggingMeta(type):
    def __new__(cls, name, bases, attrs):
        logstash_params = {}
        for item, attr_val in attrs.items():
            # item is name, attr_val is the functoin
            if isinstance(attr_val, types.FunctionType):
                attrs[item] = log_wrapper(attr_val)
            elif isinstance(attr_val, classmethod):
                # need to get the method that's wrapped with classmethod
                attrs[item] = classmethod(
                        log_wrapper(attr_val.__get__(object).__func__))
        if logstash_params:
            init_logger(**logstash_params)

        return super(LoggingMeta, cls).__new__(cls, name, bases, attrs)

# minimally invasive method: change meta of BaseClass
# won't see any decorators or any indicatoin of why
