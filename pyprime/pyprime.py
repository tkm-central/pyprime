# -*- coding: utf-8 -*-
import math

def is_definitely_prime(x: int) -> bool:
    """
    simple primarity test
    """
    if not isinstance(x, (int)):
        raise ValueError(f"{x} is not an integer")

    if x <= 0:
        raise ValueError(f"{x} is not a positive integer")
    
    if x == 1:
        return False

    _rtx = math.floor(math.sqrt(x))
    _is_prime = True
    
    for i in range(2, _rtx + 1):
        if(x % i == 0):
            _is_prime = False
            return _is_prime
    
    return _is_prime


def is_probably_prime(x: int) -> bool:
    """
    probabilistic primarity test (relatively low certainty)
    """
    raise NotImplementedError("not implemented!")


def is_certainly_prime(x: int) -> bool:
    """
    probabilistic primarity test (high certainty)
    """
    raise NotImplementedError("not implemented!")
