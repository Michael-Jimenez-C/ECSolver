import numpy as np

def SUM(*args : int | float | np.ndarray) -> int | float:
    """
    Returns the sum of two numbers.
    """
    return np.sum([np.sum(i) for i in args])


def PROD_ESCALAR(*args : int | float | np.ndarray) -> int | float:
    """
    Returns the sum of two numbers.
    """
    return np.prod([np.prod(i) for i in args])

def PROD(*args : int | float | np.ndarray) -> np.ndarray:
    """
    Returns the product of two or more numbers or arrays.
    """
    result = 1
    for i in args:
        result *= i
    return result

def MIN(*args : int | float | np.ndarray) -> int | float:
    """
    Returns the minimum value from the arguments.
    """
    return np.min([np.min(i) for i in args])

def MAX(*args : int|float|np.ndarray) -> int | float:
    """
    Returns the maximum value from the arguments.
    """
    return np.max([np.max(i) for i in args])