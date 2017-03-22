import decimal


def print_matrix(matrix):
    print("------------")
    for i in range(len(matrix)):
        print(matrix[i])
    print("------------")


def round_number(num):
    arr = str(num).split('.')
    integer = int(arr[0])
    decimals = int((arr[1])[0])
    if decimals > 0:
        if decimals > 5:
            if integer > 0:
                integer += 1
            else:
                integer -= 1
    return integer


def exponential_output(num):
    return '{:.10E}'.format(decimal.Decimal(str(num))).lower()

