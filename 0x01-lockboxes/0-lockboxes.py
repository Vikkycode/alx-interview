#!/usr/bin/python3
""" canUnlockAll function """
from collections import deque


def canUnlockAll(boxes):
    """
    determines if all boxex can be unlocked
    """

    num = len(boxes)
    open_boxes = set()

    open_boxes.add(0)

    quene = deque([0])

    while quene:
        cur_box = quene.popleft()

        keys = [k for k in boxes[cur_box] if k < num and k not in open_boxes]
        open_boxes.update(keys)
        quene.extend(keys)

    return len(open_boxes) == num
