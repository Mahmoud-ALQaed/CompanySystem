import time


def pause():
    time.sleep(8)


def invalid_type():
    print("Invalid data type")
    pause()


def validate_positive_int(value):
    if not value.isdigit():
        return False
    if int(value) <= 0:
        return False
    return True
