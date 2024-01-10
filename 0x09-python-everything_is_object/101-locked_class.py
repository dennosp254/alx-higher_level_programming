#!/usr/bin/python3
"""Defines a locked class."""

class LockedClass:
    """
    prevent the user from instanting new Lockedclass
    attributes for anything but attributes called 'first_name'.
    """
    __slots__ = ["first_name"]
