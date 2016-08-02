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
    if '/' in num:
        num_array = num.split('/')
        try:
            val = float(num_array[0]) / float(num_array[1])
            return val
        except ValueError:
            return None
    else:
        try:
            val = float(num)
            return val
        except ValueError:
            return None


def is_positive(num):
    if num > 0:
        return True
    else:
        return False
