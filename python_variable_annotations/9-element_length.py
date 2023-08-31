#!/usr/bin/env python3
"""Annotate the below functions parameters 
and return values with the appropriate types

def element_length(lst):
    return [(i, len(i)) for i in lst] """
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return list of tuples of sequence and int"""
    return [(i, len(i)) for i in lst]
