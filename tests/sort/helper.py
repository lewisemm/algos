import random

def create_randomised_array(width=10, scale=10):
    """
    Creates an array of length `width` that contains random values between
    0 and scale.
    """
    array = []
    for i in range(width):
        array.append(int(random.random() * scale))
    return array

def create_randomised_array_with_negatives(width=10, scale=10):
    """
    Creates an array of length `width` that contains a random mix of positive
    and negative values between 0 and scale.
    """
    array = []
    for _ in range(width):
        current = int(random.random() * scale)
        sign = random.choice(['-', '+'])
        if (sign == '-'):
            current = current * -1
        array.append(current)
    return array
