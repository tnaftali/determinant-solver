def is_valid_range(num_str):
    valid = True
    if not is_number(num_str):
        valid = False
    else:
        num = int(num_str)
        if not is_positive(num) or not (num > 1):
            valid = False
    return valid


def is_number(num):
    try:
        val = int(num)
        return True
    except ValueError:
        return False


def is_positive(num):
    if num > 0:
        return True
    else:
        return False
