# Documenting Subclasses
class BaseClass:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        
        # Generate documentation for the subclass based on its attributes and methods
        doc = f"{cls.__name__}\n\n"
        doc += "Attributes:\n"
        for attr in cls.__dict__:
            if not attr.startswith("__"):
                doc += f"- {attr}: {getattr(cls, attr)}\n"
        doc += "\nMethods:\n"
        for method in cls.__dict__:
            if callable(getattr(cls, method)) and not method.startswith("__"):
                doc += f"- {method}:\n"
                doc += f"  {getattr(cls, method).__doc__}\n"
        cls.__doc__ = doc

class SubClassA(BaseClass):
    """Documentation for SubClassA"""
    value = 1
    
    def method(self):
        """Documentation for method"""
        pass

print(SubClassA.__doc__)
