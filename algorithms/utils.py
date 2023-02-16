def percentage_nonzero(array):
    num_nonzero = 0
    total = 0

    for row in array:
        for element in row:
            total += 1
            if element != 0:
                num_nonzero += 1

    percentage = (num_nonzero / total) * 100

    return percentage
