import math


def square(s):

    if isinstance(s, int):
        return print(s*s)
    else:
        return print(math.ceil(s*s))


square(5.5)
