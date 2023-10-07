def count_digits(number):
    count = 0
    current = abs(number)

    while (current > 0):
        current = current // 10
        count += 1
    return count


def get_digit_at(number, position):
    if (position < 0):
        raise Exception('Invalid digit position. Should be greater than 0')
    if (position > count_digits(number)):
        return 0
    number = abs(number) // 10 ** (position - 1)
    return number % 10


def radix_sort(array):
    longest_pos, longest_neg = 0, 0
    positives, negatives = [], []

    for no in array:
        if (no >= 0):
            longest_pos = max(longest_pos, no)
            positives.append(no)
        else:
            negatives.append(no)
            longest_neg = min(longest_neg, no)
    longest_pos = count_digits(longest_pos)
    longest_neg = count_digits(longest_neg)

    current_digit = 1
    for _ in range(longest_pos):
        temp = [[] for _ in range(10)]
        for no in positives:
            digit = get_digit_at(no, current_digit)
            temp[digit].append(no)
        positives = []
        # treating each element in temp as a queue (first in first out)
        for q in temp:
            i = 0
            length = len(q)
            while (i < length):
                positives.append(q[i])
                i += 1
        current_digit += 1

    current_digit = 1
    for _ in range(longest_neg):
        temp = [[] for _ in range(10)]
        for no in negatives:
            digit = get_digit_at(no, current_digit)
            temp[digit].append(no)
        negatives = []
        for q in temp:
            i = 0
            length = len(q)
            while (i < length):
                negatives.append(q[i])
                i += 1
        current_digit += 1

    result = []
    while negatives:
        result.append(negatives.pop())
    for no in positives:
        result.append(no)

    return result
