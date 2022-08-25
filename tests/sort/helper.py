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
