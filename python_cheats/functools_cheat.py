from functools import wraps


# @wraps(func) preserves the original function's metadata (like its name and docstring),
def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"This is a decorator for {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

'''
Example:

@measure_time
def foo():
    """This is foo."""
    pass

print(foo.__name__)  # Output：foo
print(foo.__doc__)   # Output：This is foo.
'''