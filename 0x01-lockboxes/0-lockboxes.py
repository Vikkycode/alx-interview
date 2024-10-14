#!/usr/bin/python
""" canUnlockAll function """


def canUnlockAll(boxes):
    """
    determines if all boxex can be unlocked

    Returns:
    bool: True if all boxes can be unlocked otherwise return False
    """

    opened = set([0])
    closed = set(boxes[0]).difference(opened)

    while len(closed) > 0:
        key = closed.pop()

        if key not in open:
            opened.add(key)
            closed = closed.union(boxes[key]).difference(opened)

    return len(opened) == len(boxes)
