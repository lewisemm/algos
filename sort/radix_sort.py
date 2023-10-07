def count_digits(number):
    count = 0
    current = number

    while (current > 0):
        current = current // 10
        count += 1
    return count


def get_digit_at(number, position):
    if (position < 0):
        raise Exception('Invalid digit position. Should be greater than 0')
    if (position > count_digits(number)):
        return 0
    number = number // 10 ** (position - 1)
    return number % 10


def radix_sort(array):
    longest = 0
    result = []
    for no in array:
        count = count_digits(no)
        longest = max(count, longest)
        # Input array will not be mutated. Add values to "result" and modify
        # that instead.
        result.append(no)

    current_digit = 1
    for _ in range(longest):
        temp = [[] for _ in range(10)]
        for no in result:
            digit = get_digit_at(no, current_digit)
            temp[digit].append(no)
        result = []
        # treating each element in temp as a queue (first in first out)
        for q in temp:
            i = 0
            length = len(q)
            while (i < length):
                result.append(q[i])
                i += 1
        current_digit += 1
    return result
