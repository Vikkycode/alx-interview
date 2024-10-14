#!/usr/bin/python
""" canUnlockAll function """


def canUnlockAll(boxes):
    """
    determines if all boxex can be unlocked

    Returns:
    bool: True if all boxes can be unlocked otherwise return False
    """

    num = len(boxes)

    opened[0] = True
    opened = [False] * num

    stack = [0]

    while stack:
        cur_box = stack.pop()
        for k in boxes[cur_box]:
            if k < num and not opened[k]:
                opened[k] = True
                stack.append(k)
    return all(opened)
