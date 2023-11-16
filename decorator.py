from random import randint


def log(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            t = randint(10, 50)
            print(f'{text} {t} минут(ы).')
            return func(*args, **kwargs)
        return wrapper
    return decorator
