
# Define a metaclass for creating classes with logging
class LoggingMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # Create a new class for the object
        logging_class = super(LoggingMetaclass, cls).__new__(cls, name, bases, attrs)

        # Add a method for logging method calls
        def log_method_call(self, method):
            print(f'Calling method {method.__name__}')
            return method

        # Override each method in the class with a logged version of the method
        for method_name, method in attrs.items():
            if callable(method):
                setattr(cls, method_name, log_method_call(logging_class,method))

        return logging_class

# Define a base class for objects with logging
class LoggingObject(metaclass=LoggingMetaclass):
    pass

# Define a custom class with logging
class MyCustomObject(LoggingObject):
    def my_method(self, arg1, arg2):
        print('Inside my_method with arguments {}, {}'.format(arg1, arg2))

# Create an instance of the custom class
my_object = MyCustomObject()

# Call the method on the object
my_object.my_method(arg1=1, arg2=2)
