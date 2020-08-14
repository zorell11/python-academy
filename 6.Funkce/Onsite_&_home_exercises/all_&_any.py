#!/usr/bin/env python3

def my_all(seq):
    if seq == []:
        return True

    else:
        for i in seq:
            if not bool(i):
                return False
    return True


def my_any(seq):
    if seq == []:
        return False

    else:
        for i in seq:
            if bool(i):
                return True
    return False
