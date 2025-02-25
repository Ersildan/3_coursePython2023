import functools

def prefix(string, to_the_end=False):
    def decorator(func):   
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            if to_the_end:
                return f"{value} {string}"
            return f"{string} {value}"
        return wrapper
    return decorator
