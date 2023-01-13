#!/usr/bin/python3
"""
Contains a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Returns the fewest number of operations needed to result in exactly
    n H characters in the file.
    """
    operations = 0
    minops = 2
    while n > 1:
        while n % minops == 0:
            operations += minops
            n /= minops
        minops += 1
    return operations
