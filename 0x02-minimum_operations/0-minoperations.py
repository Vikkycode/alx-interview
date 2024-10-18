#!/usr/bin/env python3
"""Min Operations """



def minOperations(n):
    """
    Calculates the few number of operations needed to result
    in exactly n H characters in the file.

    Args:
        n: The target number of 'H' characters.

    Returns:
        The minimum number of operations, or 0 if impossible.
    """

    if n <= 1:
        return n

    operations = 0
    n_h = 1
    clipboard = 1

    while n_h < n:
        if n % n_h == 0:  
            clipboard = n_h
            operations += 1
        
        n_h += clipboard
        operations += 1

    return operations
