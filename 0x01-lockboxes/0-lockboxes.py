#!/usr/bin/python3
"""
a method that determines if all the boxes can be opened.
"""

def canUnlockAll(boxes):
    """
    a method that determines
    if all the boxes can be opened
    """
    # Initialize a set to keep track of unlocked boxes
    unlocked = set([0])

    # Initialize a list to keep track of keys we have
    keys = []
    keys.extend(boxes[0])

    # While we have keys, try to unlock boxes
    while keys:
        key = keys.pop()
        # If the key corresponds to a box and the box is not unlocked yet
        if key < len(boxes) and key not in unlocked:
            # Unlock the box and add its keys to our keys list
            unlocked.add(key)
            keys.extend(boxes[key])

    # If the number of unlocked boxes is equal to the number of boxes, return True
    return len(unlocked) == len(boxes)
