def print_matrix(matrix):
    print "------------"
    for i in range(len(matrix)):
        print matrix[i]
    print "------------"


def round_number(num):
    arr = str(num).split('.')
    whole = int(arr[0])
    decimals = int((arr[1])[0])
    if decimals > 0:
        if decimals > 5:
            if whole > 0:
                whole += 1
            else:
                whole -= 1
    return whole
