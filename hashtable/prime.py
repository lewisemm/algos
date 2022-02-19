def generate_prime(target):
    """
    Generates the greatest prime number that is less than `target`.
    """
    primes = [2, 3, 5, 7]
    length = len(primes)
    current = primes[-1] + 2
    yaah = primes[-1]

    while current < target:
        is_prime = True
        for prime in primes:
            if current % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(current)
        current += 2
    return primes[-1]
