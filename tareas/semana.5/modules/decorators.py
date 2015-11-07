from functools import wraps


def typeint(func):
    """
    Decorator retorna solo entero de una funcion
    :param func:
    :type func:
    :return:
    :rtype:
    """

    @wraps(func)
    def wrapper(arg):
        ret = func(arg)
        return int(ret)

    return wrapper
