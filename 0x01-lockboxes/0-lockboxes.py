#!/usr/bin/python
""" canUnlockAll function """
from collections import deque


def canUnlockAll(boxes):
    """
    determines if all boxex can be unlocked

    Returns:
    bool: True if all boxes can be unlocked otherwise return False
    """

    num = len(boxes)
    open_boxes = set()
    open_boxes.add(0)

    quene = deque([0])

    while quene:
        curr_box = quene.popleft()

        for key in boxes[curr_box]:
            if key < num and key not in open_boxes:
                open_boxes.add(key)
                quene.append(key)

    return len(open_boxes) == num