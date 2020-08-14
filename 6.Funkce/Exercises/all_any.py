def my_all(sequence):
    for item in sequence:
        if not item:
            return False
    return True


def my_any(sequence):
    for item in sequence:
        if item:
            return True
    return False

print(my_all([]))
