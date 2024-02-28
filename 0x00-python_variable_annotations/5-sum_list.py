#!/usr/bin/env python3
""" annotations types - list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Returns sum of floats of list """
    sum_float: float = 0
    for i in input_list:
        sum_float += i

    return sum_float
