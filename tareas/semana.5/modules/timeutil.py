import math as mah
from modules.decorators import typeint


@typeint
def seconds(ms):
    """
    Transforma milisegundo(s) a segundo(s)
    :param ms:
    :type ms:
    :return: Segundo(s)
    :rtype: int
    """
    return ms / 1000

@typeint
def minutes(s: int) -> int:
    """
    Transforma segundo(s) a minutos(s)
    :param s:
    :type s:
    :return:
    :rtype:
    """
    return s / 60


def hours(m: int) -> int:
    """
    Transforma minuto(s) a hora(s)
    :param m:
    :type m:
    :return:
    :rtype:
    """
    return mah.floor(m / 60)


def days(hr: int) -> int:
    """
    Transforma hora(s) a dia(s). Resultado es un entero mas grande pero menor o igual `hr`
    :param hr: Hora(s)
    :type hr: int
    :return: Dia(s)
    :rtype: int
    """
    return mah.floor(hr / 24)
