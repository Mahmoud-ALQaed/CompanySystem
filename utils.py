import time

def pause():
    time.sleep(5)

def validate_positive_int(value):
    if not value.isdigit():
        return False
    if int(value) <= 0:
        return False
    return True

def validate_name(value):
    if value:
        return True

def validate_age(value):
    if not value.isdigit():
        return False
    if int(value) < 18:
        return False
    return True

def validate_bonus(value):
    if not value.isdigit():
        return False
    if int(value) < 0:
        return False
    return True
