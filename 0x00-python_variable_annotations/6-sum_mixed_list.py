#!/usr/bin/env python3
""" annotations type - Mixed lists"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ Returns float of the sum of interges and floats """
    sum_total: float = 0
    for i in mxd_list:
        sum_total += i

    return sum_total
