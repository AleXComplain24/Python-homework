import inspect
import json


def introspection_info(obj):
    """
    Function to inspect an object and return detailed information about it.
    """
    obj_type = type(obj).__name__
    all_attributes = dir(obj)
    methods = [attr for attr in all_attributes if callable(getattr(obj, attr, None))]
    attributes = [attr for attr in all_attributes if not callable(getattr(obj, attr, None))]
    obj_module = getattr(obj, '__module__', 'Built-in/No module')
    is_callable = callable(obj)
    docstring = inspect.getdoc(obj) if inspect.isclass(obj) or inspect.ismethod(obj) or inspect.isfunction(
        obj) else None

    return {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module,
        'callable': is_callable,
        'docstring': docstring
    }


# Create introspection data
number_info = introspection_info(42)


# Define a custom class
class SampleClass:
    """This is a sample class for testing introspection."""

    def __init__(self, value):
        self.value = value

    def greet(self):
        return f"Hello, {self.value}!"


sample_instance = SampleClass("World")
class_info = introspection_info(sample_instance)

# Print results in readable format
print("Introspection of an integer:")
print(json.dumps(number_info, indent=4))

print("\nIntrospection of a custom class instance:")
print(json.dumps(class_info, indent=4))

print(number_info)
